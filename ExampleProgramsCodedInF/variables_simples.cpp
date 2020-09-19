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
    int potencia;
    potencia = x;
    int j;
    double num,den;
    num=0;
    den=0;
    for(j=0;j<11;j=j+1){
        y=j;
        x=potencia;
        power();
        num = res;
        m = j;
        f=1;
        factorial();
        den = f;
        print(num);
        print("/");
        print(den);
        print("endl");
        valorE  = valorE + (num/den);
    }
    print("RESULTADO:");
    print(valorE);
    print("endl");
}
main(){
    
    do{
        print("--MENU--");
        print("endl"); 
        print("1) Factorial");
        print("endl");
        print("2) Potencia");
        print("endl");
        print("3) e^x");
        print("endl");
        print("0) Salir");
        print("endl");
        read(opcion);
        f=1;
        if(opcion == 1){
            print("Introduce el numero para  factorial");
            print("endl");
            uno();
            factorial();
            dos();
        }
        if(opcion == 2){
            print("Introduce x para power");
            print("endl");
            read(x);
            print("Introduce y para power");
            print("endl");
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