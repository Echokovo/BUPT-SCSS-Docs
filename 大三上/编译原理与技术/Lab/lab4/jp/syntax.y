%{
    #include"lex.yy.c"
    void yyerror(const char*);
%}

%token LC RC LB RB COLON COMMA
%token STRING NUMBER
%token TRUE FALSE VNULL

%nonassoc ERR
%left RB COMMA
%%

Json:
      Value
    ;
Value:
      Object
    | Array
    | STRING
    | NUMBER
    | TRUE
    | FALSE
    | VNULL
    ;
Object:
      LC RC
    | LC Members RC
    | LC Members RC STRING error { puts("Extra value after close, recovered"); }
    ;
Members:
      Member
    | Member COMMA Members
    | Member COMMA RC error { puts("Extra comma, recovered"); }
    | Member COMMA error { puts("Comma instead if closing brace, recovered"); }
    ;
Member:
      STRING COLON Value %prec ERR
    | STRING COMMA Value error { puts("Comma instead of colon, recovered"); }
    | STRING COLON NUMBER NUMBER error { puts("Numbers cannot have leading zeroes, recovered"); }
    | STRING Value error { puts("Missing colon, recovered"); }
    | STRING COLON COLON Value error { puts("Double colon, recovered"); }
    ;
Array:
      LB RB
    | LB Values RB %prec ERR
    | LB Values error { puts("Unclosed array, recovered"); }
    | LB Values RB COMMA error { puts("Comma after the close, recovered"); }
    | LB Values RB RB error { puts("Extra close, recovered"); }
    | LB Values RC error { puts("mismatch, recovered"); }
    ;
Values:
      Value
    | Value COMMA Values
    | Value COLON Values error { puts("Colon instead of comma, recovered"); }
    | Value COMMA error { puts("extra comma, recovered"); }
    | Value COMMA COMMA error { puts("double extra comma, recovered"); }
    | COMMA Values error { puts("missing value, recovered"); }
    ;

%%

void yyerror(const char *s){
    printf("syntax error: ");
}

int main(int argc, char **argv){
    if(argc != 2) {
        fprintf(stderr, "Usage: %s <file_path>\n", argv[0]);
        exit(-1);
    }
    else if(!(yyin = fopen(argv[1], "r"))) {
        perror(argv[1]);
        exit(-1);
    }
    yyparse();
    return 0;
}
