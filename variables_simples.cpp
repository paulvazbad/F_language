int x,f,y;
int res;
int opcion;
function uno(){
    read(x);
}
function dos(){
    print(f);
}
function tres(){
    if(x>1){
        f = f*x;
        x =x-1;
        tres();
    }
}
function power(){
    int i;
    for(i=0 ;i<y; i= i+1){
        res = res * x;
    }
}

main(){
   print("Introduce x para factorial");

    f = 1;
    uno();
    tres();
    dos();
    res=1;
    read(x);
    read(y);
    power();
    print(res);
}