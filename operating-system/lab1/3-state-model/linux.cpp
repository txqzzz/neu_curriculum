/*************************************************************************
     File Name: linux.cpp
     Author: Xingqi Tang
     ################### 
     Mail:xingqitang@gmail.com
     Created Time: Wed Apr  4 15:11:32 2018
 ************************************************************************/
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<cstring>
#include<map>
#include<queue>
#include<stack>
#include<string>
#include<cstdlib>
#include<ctime>
#include<set>
using namespace std;
 /*MACRO*/
#define FORi(l,r) for(int i=(l);i<(r);i++)
#define FORj(l,r) for(int j=(l);j<(r);j++)
#define FORk(l,r) for(int k=(l);k<(r);k++)
#define MEMSET0(i) memset((i),0,sizeof((i)))
#define MEMSET1(i) memset((i),-1,sizeof((i)))


// THIS CODE IS THE SIMULTION OF THE MENTIONED PROJECT IN LINUX OS



#include <sys/time.h>
#include<math.h>
#include<stdlib.h>
#include<time.h>

using namespace std;

 typedef struct process
 {
     int pid;
     double cut,irt,wt;
     double rq_t;
 };



void createProcess();
double callExec(process);
double accessIOQ(process);


// GLOBAL VARIABLES
process p;
int k=0;
int count_p = 0;
int count_z = 0;

struct timeval t1, t2;
double elapsedTime;


// QUEUE DECLARATION
queue <process> readyqueue;
queue <process> ioqueue;
queue <process> finqueue;
queue <process> tempqueue;

// MAIN FUNCTION
int main()
{
    int num;
    while(1)
    {
        cout<<endl<<"____________________"<<endl;
        createProcess();
        count_p++;
        if(count_z==25)
            break;
    }
    //cout<<endl<<"tot proc:"<<count_p;
    //cout<<finqueue.size();
    //cout<<ioqueue.size();
}


// PROCESS CREATION
void createProcess()
{
    //process p ;
    p.pid = ++k;
    p.cut=0;
    p.irt=0;
    p.wt=0;
    p.rq_t=0;

    readyqueue.push(p);

    gettimeofday(&t1, NULL);

    readyqueue.front().cut += callExec(readyqueue.front());
   //cout<<endl<<readyqueue.front().cut<<endl;
   //cout<<endl<<readyqueue.size()<<endl;

    srand(time(NULL));
    int r = (p.pid+rand()) % 3;

    //cout<<endl<<"random "<<r<<endl;
    if(r==0)
        count_z++;

    switch(r)
    {
    case 0:

	gettimeofday(&t2, NULL);

        // compute and print the elapsed time in millisec
        elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000.0;      // sec to ms
        elapsedTime += (t2.tv_usec - t1.tv_usec)/1000.0 ;   // us to ms
        
	p.rq_t = elapsedTime;
	//cout<<endl<<"size "<<readyqueue.size();
        //cout<<endl<<"front pid"<<readyqueue.front().pid;
        //cout<<endl<<"rq_t:"<<p.rq_t<<endl;
        readyqueue.front().wt += p.rq_t   ;
        finqueue.push(readyqueue.front());
        cout<<endl<<"Process ID (PID): "<<readyqueue.front().pid;
        cout<<endl<<"CPU Usage time(CUT) : "<<readyqueue.front().cut;
        cout<<endl<<"IO time(IRT) : "<<readyqueue.front().irt;
        cout<<endl<<"Waiting time(WT) : "<<readyqueue.front().wt<<endl;
        readyqueue.pop();
        //cout<<endl<<"after popping pid "<<readyqueue.front().pid;
        break;
    case 1:
        tempqueue.push(readyqueue.front());
        readyqueue.pop();
        readyqueue.push(tempqueue.front());
        tempqueue.pop();
        //cout<<endl<<"from the back:"<<readyqueue.back().pid<<endl;
        break;
    case 2:
        readyqueue.front().irt+=accessIOQ(readyqueue.front());
        tempqueue.push(readyqueue.front());
        ioqueue.push(readyqueue.front());
        readyqueue.pop();
        readyqueue.push(tempqueue.front());
        tempqueue.pop();
        break;
    }
}

// PROCESS EXECUTION
double callExec(process p)
{

    srand(time(NULL));
    int r = rand() % 10000;
    double elapsedTime;
    int i,j;

    // start timer
    gettimeofday(&t1, NULL);

    for(i=0;i<r;i++)
        j=sin(i);

    gettimeofday(&t2, NULL);

    // compute and print the elapsed time in millisec
    elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000.0;      // sec to ms
    elapsedTime += (t2.tv_usec - t1.tv_usec)/1000.0 ;   // us to ms
    //cout << p.t2 << " ms.\n";
    p.cut = elapsedTime;    
    return p.cut;
}


//PROCESS IN IO QUEUE
double accessIOQ(process p)
{
    srand(time(NULL));
    int r = (p.pid+rand()) % 100;
    p.irt=r;
    return p.irt;
}
