%{
    #include"lex.yy.c"
    void yyerror(const char *s){}
    int result;
%}
%token LP RP LB RB LC RC
%%
String: %empty {result = 1;}
    | Expr {result = 1;}
    | error {result = 0;}
    ;
Expr: Pair
    | Expr Pair
Pair: LP RP
    | LB RB
    | LC RC
    | LP Expr RP
    | LB Expr RB
    | LC Expr RC
    ;
%%

int validParentheses(char *expr){
    yy_scan_string(expr);
    yyparse();
    return result;
}
