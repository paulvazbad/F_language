int x,f,y,m;
int res;
int opcion;
int valorE;
function uno(){
    read(m);
}
function dos(){
    print(f);
}
function tres(){
    if(m>1){
        f = f*m;
        m =m-1;
        tres();
    }
}

function factorial(){
    tres();
}

function power(){
    int i;
    res = 1;

    for(i=0 ;i<y; i= i+1){
        res = res * x;
    }
}

function e(){
    print("Introduce x para e^x");
    read(x);
    int j;
    double num,den;
    num=0;
    den=0;
    for(j=0;j<10;j=j+1){
        y=j;
        power();
        num = res;
        m = j;
        factorial();
        den = f;
        valorE  = valorE + (num/den);
    }
    print("RESULTADO:");
    print(valorE);
}
main(){
    
    do{
        print("--MENU--"); 
        print("1) Factorial");
        print("2) Potencia");
        print("3) e^x");
        print("0) Salir");
        read(opcion);
        f=1;
        if(opcion == 1){
            print("Introduce el numero para  factorial");
            uno();
            factorial();
            dos();
        }
        if(opcion == 2){
            print("Introduce x para power");
            read(x);
            print("Introduce y para power");
            read(y);
            power();
            print(res);
        }
        if(opcion == 3){
            e();
        }

    }while(opcion!=0);
    print("Adios!");
    
}