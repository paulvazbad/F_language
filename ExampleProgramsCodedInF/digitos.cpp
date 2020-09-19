int numero;
int original;
int residuo;

function imprimirRes(){
    if(residuo==1){
        print("uno");
    }
    if(residuo==2){
        print("dos");
    }
    if(residuo==3){
        print("tres");
    }
    if(residuo==4){
        print("cuatro");
    }
    if(residuo==5){
        print("cinco");
    }
    if(residuo==6){
        print("seis");
    }
    if(residuo==7){
        print("siete");
    }
    if(residuo==8){
        print("ocho");
    }
    if(residuo==9){
        print("nueve");
    }
    print("endl");
} 

function digito(){
    while(numero>0){
        original = numero;
        numero = numero/10;
        residuo = original - (numero*10);
        imprimirRes();
    }
}

main(){
    print("dame el numero");
    print("endl");
    read(numero);
    digito();
}