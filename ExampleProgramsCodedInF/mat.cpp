double tictactoe[3][3][2];
int a,i,j,value, pieza;
int temp;

function llenar(){
    value=0;
    for(i=0;i<3;i=i+1){
        for(j=0;j<3;j=j+1){
            value = i-j;
            tictactoe[i][j][0]=value;
            value = i+j;
            tictactoe[i][j][1]=value;
            
        }
        
    }

}

function imprimir(){
    for(i=0;i<3;i=i+1){
        for(j=0;j<3;j=j+1){
            value  = tictactoe[i][j][0];
            print(value);
            print(" ");
        }
        print("endl");
    }
}
function dosimprimir(){
    for(i=0;i<3;i=i+1){
        for(j=0;j<3;j=j+1){
            value  = tictactoe[i][j][1];
            print(value);
            print(" ");
        }
        print("endl");
    }
}
function sumar(){
    for(i=0;i<3;i=i+1){
        for(j=0;j<3;j=j+1){
            value  = tictactoe[i][j][1] + tictactoe[i][j][0];
            print(value);
            print(" ");
        }
        print("endl");
    }
}
main(){
   print("Primera dimension");
   print("endl");
   llenar();
   imprimir();
   print("Segunda dimension");
   print("endl");
   dosimprimir();
   print("Suma de ambas");
   print("endl");
   sumar();
}