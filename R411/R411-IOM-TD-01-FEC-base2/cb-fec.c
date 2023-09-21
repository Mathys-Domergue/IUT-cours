// apt install cmake pkg-config libliquid-dev
// rm -rf CMakeFiles/ CMakeCache.txt && cmake . && make
#include <stdio.h>
#include <time.h>// cb
#include <unistd.h>// cb getpid()
#include <stdlib.h>
#include <string.h>
#include <getopt.h>

#include <liquid/liquid.h>

///////////////////////////////////////////////////////////////////////////////
void printData(unsigned char *data,int len,char *header) {
  printf("%20s:  [%3u] ",header,len);
  for (int i=0;i<len;i++) {
    printf(" %02X",(unsigned int)(data[i]));
  }
  printf("\n");
}
///////////////////////////////////////////////////////////////////////////////
void printData2(unsigned char *data,unsigned char *dataRef,int len,char *header) {
  printf("%20s:  [%3u] ",header,len);
  for (int i=0;i<len;i++) {
    if (data[i]!=dataRef[i]) {
      printf(" \033[31m%02X\033[0m",(unsigned int)(data[i]));//red
    } else {
      printf(" %02X",(unsigned int)(data[i]));
    }
  }
  printf("\n");
}
///////////////////////////////////////////////////////////////////////////////
// print usage/help message
void usage() {
    printf("cb-fec [options]\n");
    printf("  -u/h         : print usage\n");
    printf("  -e number    : error number (default 3)\n");// cb
    printf("  -k size      : random input data size (default 4)\n");
    printf("  -m asciiMsg  : input ascii message\n");
    printf("  -l loop      : loop number (default 1)\n");
    printf("  -c scheme    : coding scheme (default h74)\n");
    liquid_print_fec_schemes();
}
///////////////////////////////////////////////////////////////////////////////
int main(int argc, char*argv[]) {
    unsigned int loop=1;
    unsigned int err=3;                   // cb - error number
    unsigned int n=4;                     // data length (bytes)
    unsigned int nmax=1024;               // maximum data length
    char msg[nmax+1];                     // message
    unsigned int msgLen=0;
    fec_scheme fs=LIQUID_FEC_HAMMING74;   // error-correcting scheme
    int dopt;
    msg[0]=0;// null message at start
    while((dopt=getopt(argc,argv,"uhe:l:m:k:c:"))!=EOF) {// cb
      switch (dopt) {
        case 'h':
        case 'u': usage(); return 0;
        case 'e': err=atoi(optarg); break;// cb
        case 'k': n=atoi(optarg); break;
        case 'l': loop=atoi(optarg); break;
        case 'm': strncpy(msg,optarg,nmax);msg[nmax]=0;msgLen=strlen(msg);break;
        case 'c':
            fs=liquid_getopt_str2fec(optarg);
            if (fs == LIQUID_FEC_UNKNOWN) {
                fprintf(stderr,"Error: unknown/unsupported FEC scheme \"%s\"\n\n",optarg);
                exit(1);
            }
            break;
        default:
            exit(1);
      }
    }
    // ensure proper data length
    if (msgLen>0) n=msgLen;
    n=(n>nmax)?nmax:n;
    srand(time(NULL)+getpid());// cb
    unsigned int n_enc=fec_get_enc_msg_length(fs,n);
    printf("Error number: %u\n",err);
    printf("Msg length  : %u\n",n);
    printf("Encoded msg : %u\n",n_enc);
    unsigned char data[n];          // original data message
    unsigned char msg_enc[n_enc];   // encoded data message
    unsigned char msg_cor[n_enc];   // corrupted data message
    unsigned char msg_dec[n];       // decoded data message
    int err_byte[err];              // byte position
    int err_bit[err];               // bit position
    // create object
    fec q=fec_create(fs,NULL);
    fec_print(q);
    unsigned int i;
    unsigned total_num_sym_errors=0,total_num_bit_errors=0;
    for (int x=0;x<loop;x++) {
      // create message
      for (i=0;i<n;i++) {
        if (msgLen>0) data[i]=msg[i];
        else data[i]=rand()&0xff; // random if no msg given
      }
      // encode message
      fec_encode(q,n,data,msg_enc);
      // corrupt encoded message
      memmove(msg_cor,msg_enc,n_enc);
      for (int k=0;k<err;k++) {// cb
        err_byte[k]=rand()%n_enc;   //byte position
        err_bit[k]=rand()%8;        //bit position
        printf("Error bit %d octet %d \n",err_bit[k],err_byte[k]);
        msg_cor[err_byte[k]]^=(1<<err_bit[k]);
      }
      // decode message
      fec_decode(q,n,msg_cor,msg_dec);
      printData(data,n,"Original message");
      printData(msg_enc,n_enc,"Encoded message");
      printData2(msg_cor,msg_enc,n_enc,"Corrupted message");
      printData2(msg_dec,data,n,"Decoded message");
      if (msgLen>0) {
        printf("Input ASCII message : [%s]\n",msg);
        for (i=0;i<n;i++) msg[i]=msg_dec[i];
        printf("Output ASCII message: [%s]\n",msg);
      }
      // count bit errors
      unsigned int j,num_sym_errors=0,num_bit_errors=0;
      unsigned char e;
      for (i=0;i<n;i++) {
        num_sym_errors+=(data[i]==msg_dec[i])?0:1;
        e=data[i]^msg_dec[i];
        for (j=0;j<8;j++) {
          num_bit_errors+=e&0x01;
          e>>=1;
        }
      }
      total_num_sym_errors+=num_sym_errors;
      total_num_bit_errors+=num_bit_errors;
      //printf("number of symbol errors detected: %d\n", num_errors_detected);
      printf("number of symbol errors received: %3u / %3u\n",num_sym_errors,n);
      printf("number of bit errors received:    %3u / %3u\n",num_bit_errors,n*8);
    }
    printf("Total number of symbol errors received: %3u / %3u\n",total_num_sym_errors,loop*n);
    printf("Total number of bit errors received:    %3u / %3u\n",total_num_bit_errors,loop*n*8);
    // clean up objects
    fec_destroy(q);
    return 0;
}

