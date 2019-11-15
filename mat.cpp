double tictactoe[3][3][2];
int a,i,j,value, pieza;
int temp;

function llenar(){
    value=0;
    for(i=0;i<3;i=i+1){
        for(j=0;j<3;j=j+1){
            if(i==1 && j==1){
                value=1;
            }
            else{
                value=0;
            }
            tictactoe[i][j][0]=value;
            
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
main(){
   llenar();
   imprimir();
}