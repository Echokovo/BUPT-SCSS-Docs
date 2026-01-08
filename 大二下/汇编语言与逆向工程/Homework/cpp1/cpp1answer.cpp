# include<iostream>
int main(){
    int s[]={0x52,0xC7,0xC2,0xCD,0xEE,0xEB,0xFE,0xF5};
    int x[]={0x6,0x7,0x8,0x9,0xA,0xB,0xC,0xD};
    for(int i=0;i<8;i++)
        s[i]^=x[i];
    for(int i=0;i<8;i++){
        int b=s[i];
        int b8=b&0x80;
        int b72=b&0x7E;
        int b1=b&0x1;
        b8=b8>>7;
        b1=b1<<7;
        s[i]=b8|b72|b1;
        printf("%c",s[i]);
    }
    return 0;
}