int matRes[100][100];
int size1, size2;
int suma=0;
function pedirElementos(){
    int i,j,m=0;
    double r = i/2;

    for(i=0; i<size1/2;i=i+1){
        for(j=0;j<size2;j=j+1){
           while(m<2){
               read(value);
               suma = suma + value;
               m++;
           }
           a = (((b*3)-5)+2)/5;
           matRes[i][j] = suma;
           print(matRes[i][j]);
        }
    }
}
function pedirTamano(){   
    do{
       print("Dame el tamano de la matrix1");
       read(size1);
       print("Dame el tamano de la matrix2");
       read(size2);
       
    }while(size1!=size2);
}

main(){
    pedirTamano();
    pedirElementos();
}