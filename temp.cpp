
//把flagCom1ReceiveStatus修改成flagECIComReceiveStatus
//把flagCom2ReceiveStatus修改成flagTBComReceiveStatus
//把str_port1 修改成 strECIport
//把str_port2 修改成 strTBport
//增加了ivec_TBport

LRESULT CMainDlg::OnCommunication(WPARAM ch, LPARAM port)
{
	CString strTemp;
	strTemp.Format(_T("%c"),ch);
	static string strECIport("");
	static string strTBport("");

	if(port == gECIComPortNumber)
	{
		switch(flagECIComReceiveStatus)
		{
			case 0:
					strECIport += strTemp;
					if(ch == 0x0D)	flagECIComReceiveStatus = 1;
					break;
			case 1:
					strECIport += strTemp;
					if(ch==0x0A)
					{
						ivec_ECIport.push_back(strECIport);
						//todo:注意没有'\0'结束，是否构成问题?
						strECIport.clear();
						timeStart = GetTickCount();
					}
					flagECIComReceiveStatus = 0;
					break;
			default:
					break;

		}

	}
	else if(port == gTBComPortNumber)
	{
		switch(flagTBComReceiveStatus)
		{
			case 0:
					strTBport += strTemp;
					if(ch == 0x0D)	flagTBComReceiveStatus = 1;
					break;
			case 1:
					strTBport += strTemp;
					if(ch==0x0A)
					{
						ivec_TBport.push_back(strTBport);
						//todo:注意没有'\0'结束，是否构成问题
						strTBport.clear();
				//		timeStart = GetTickCount();
					}
					flagTBComReceiveStatus = 0;
					break;
			default:
					break;
		}
	}
	return 0;
}

// 接收到的字符串为strTBport



void CMainDlg::SendCommandToECITB(uint8_t command)
{
	//给ECI测试台发送测试命令，然后接收返回的数据，如果返回的数据错误，则重复发送

	//step1:打包命令存入ivec当中。
	vector<uint8_t> ivec;		
	uint8_t inputData[1] = {command};
	ivec.clear();
	packDataAndCommand(COMMAND,inputData,1,ivec);
	bool flagOvertime;
	bool flagSendtoTBSuccess;
	uint8_t receiveCommand;

	//step2:检测串口是否打开
	if(m_flagTBComOpen = false)
	{
		cout<<"与ECI测试台相连的串口没有打开，不能发送命令！\n"<<endl;
		return;
	}
	//step3:发送命令到串口，并且确保发送成功
	//flag发送没成功
	flagSendtoTBSuccess = false;
	flagOvertime = false;
	while(!flagSendtoTBSuccess)
	{
		//发送命令到串口
		m_ComPort[1].WriteToPort(&ivec[0],ivec.size());	
		//todo:这个串口只是简单的m_ComProt[1]吗？
		timeStart = GetTickCount();	
		while(ivec_TBport.size()==0&&!flagOvertime)
		{
			timeEnd = GetTickCount();	
			if(timeEnd-timeStart>2000)	//判断有无超时
				flagOvertime = true;
			else
				sleep(10);
		}

		if(ivec_TBport.size()!=0)
		{
			//接收到的字符串为ivec_TBport[0]
			//解析接收到的字符串
			int i = unpackDataAndCommand(ivec_TBport[0],receiveCommand);
			if(receiveCommand == command && i==COMMAND_OK)
			{
				flagSendtoTBSuccess = true;
			}
		}
	}
}

#include <sstream>

//在C++中更推荐使用流对象来实现类型转换。

void int2str(const int int_temp, string &string_temp)
{
	stringstream stream;
	stream<<int_temp;
	stream>>string_temp;
//	string_temp = stream.str();
}

void str2int(const string string_temp, int & int_temp)
{
	stringstream stream(string_temp);
	stream>>int_temp;
}

void str2int(const string string_temp, int & int_temp)
{
	int_temp = atoi(string_temp.c_str());
}




CString CommandText(uint8_t command)
{
	switch(command)
	{
		case SELFCHECK1: return (_T("SELFCHECK1"));
		case SELFCHECK2: return (_T("SELFCHECK2"));
		case SELFCHECK3: return (_T("SELFCHECK3"));
		case SEFLCHECK4: return (_T("SEFLCHECK4"));
		case CC200: 	return (_T("CC200"));
		case CO200: 	return (_T("CO200"));
		case NV200: 	return (_T("NV200"));
		case CC1500: 	return (_T("CC1500")); 
		case CO1500: 	return (_T("CO1500"));
		case NV1500: 	return (_T("NV1500"));
		case CC2500: 	return (_T("CC2500"));
		case CO2500: 	return (_T("CO2500"));
		case NV2500: 	return (_T("NV2500"));
		case TPS: 		return (_T("TPS"));
		case SWITCHTOROM: return (_T("SWITCHTOROM"));
		case SWITCHTORAM: return (_T("SWITCHTORAM"));
		default:		return(_T("Command Error!"));
	}
}




/***************将2个BYTE的Char转换成3个Byte的Int***********************【测试通过】*/
//如将"ff"转换成"255", "0e"转换成"014"
#include "stdafx.h"
#include <assert.h>
#include <iostream>

using namespace std;

void TwoByteCharTo3ByteInt(const char inputA,const char inputB,char &outputC, char &outputD,char &outputE);
void StringChange(const string command, string &commandNew);
void main(void)
{
	char A = 'f';
	char B = 'f';
	char C,D,E;
	TwoByteCharTo3ByteInt(A,B,C,D,E);
	cout<<"Input: "<<A<<B<<endl;
	cout<<"Output: "<<C<<D<<E<<endl;
	getchar();

}

void TwoByteCharTo3ByteInt(const char inputA,const char inputB,char &outputC, char &outputD,char &outputE)
{
	int a=0,b=0,result = 0;

	if(inputA>='0' && inputA<='9')		a = inputA-'0';
	else if(inputA>='a' && inputA<='f')	a = inputA -'a'+10;
	else if(inputA>='A' && inputA<='F')	a = inputA - 'A'+10;
	else assert(0);

	if(inputB>='0' && inputB<='9')		b = inputB-'0';
	else if(inputB>='a' && inputB<='f')	b = inputB -'a'+10;
	else if(inputB>='A' && inputB<='F') b = inputB - 'A'+10;
	else assert(0);

	result = 16*a + b;

	outputC = result/100 + '0';
	result 	= result - (result/100)*100;
	outputD = result/10 + '0';
	outputE = result%10 + '0';
}

void StringChange(const string command, string &commandNew)
{
	int length = strlen(command);
	char outputC,outputD,outputE;
	commandNew.clear();
	
	for(int i=0,j=0;i<length;)
	{
		TwoByteCharTo3ByteInt(command[i],command[i+1],outputC,outputD,outputE);
		i = i+2;
		commandNew[j++] = outputC;
		commandNew[j++] = outputD;
		commandNew[j++] = outputE;
	}
	commandNew[j] = '\0';
}
/****************************************E N D***************************************/



bool OpenCom(UINT i)			//打开第i个串口，其中i=ECICOM或者TBCOM。当i=ECICOM时，指的是与ECIBox连接的串口；当i=TBCOM时，指的是与测试工装连接串口
{
	BOOL bComSuccess = FALSE;	//COM1打开成功
	ComPortInfo portInfo;
	UINT portnr;

	if((i!=ECICOM)&&(i!=TBCOM))
	{
		MessageBox(0,"试图打开未定义的串口号，请打开与ECI连接的串口或者与测试工装连接的串口！\n","警告",0);
		return false;
	}

	while(!bComSuccess)			//除非COM1都打开了，否则就一直处理
	{	
		//获取串口信息
		portnr = GetPortInformation(i,portInfo);

		//如果没有获得串口号,则弹出对话框表示需要配置串口，再弹出配置对话框
		if(portnr==-1)			
		{
			 CString str;
			 str = _T("与ECIBox连接的串口尚未配置，请配置串口！");
			 AfxMessageBox(str);
			 return false;
			 //弹出配置窗口,以便进行串口信息配置！
			// OnBnClickedInfo();	 
		}

		if(m_ComPort[i].InitPort(this ,portnr,com_baudrate,com_parity,com_databits,com_stopbits,EV_RXFLAG|EV_RXCHAR,com_writeBufferSize))//初始化成功
		{
			 m_ComPort[i].StartMonitoring();                       //启动串口监视线程
			 CString str;
			 if(i==ECICOM)
			 {
				// str.Format(_T("COM%d打开成功！该串口与ECIBox连接！"),portnr);
				 this->m_flagECIComOpen = true;
				 this->SetPic(GetDlgItem(IDC_PIC_COM1),IDB_OK);
				 MessageBox("连接ECI的串口打开成功！","提示");
			 }
			 if(i==TBCOM)
			 {
				 // str.Format(_T("COM%d打开成功！该串口与测试工装连接！"),portnr);
				  this->m_flagTBComOpen = true;
				  this->SetPic(GetDlgItem(IDC_PIC_COM2),IDB_OK);
				  MessageBox("连接测试工装的串口打开成功！","提示");
			 }
			 bComSuccess = TRUE;
			// AfxMessageBox(str); 
			 ShowEditText(str);
			// m_showList.AddString(str); //todo:2016年5月17日注释掉，其实应该复原的！
			 //在编辑框中显示
			 str.Format(_T("portnr=%d,com_baudrate=%d,com_parity=%c,com1_databits=%d,com_stopbits=%d,com_writeBufferSize=%d"),portnr,com_baudrate,com_parity,com_databits,com_stopbits,com_writeBufferSize);
			//AfxMessageBox(str);
			 ShowEditText(str);
			// m_showList.AddString(str);  //todo:2016年5月17日注释掉，其实应该复原的！
			 //m_showList.SetCurSel(m_showList.GetCount()-1);//todo:2016年5月17日注释掉，其实应该复原的！
			}
			else                                                                                                                                                                                                                                                                                          //初始化失败
			{
				 CString str;
				 str.Format( _T("COM%d没有发现，或被其他设备占用！COM%d 打开失败！该串口应该与ECIBox连接！") ,portnr,portnr);
				 AfxMessageBox(str);
				 //弹出配置窗口,以便重新进行串口信息配置！
				 OnBnClickedInfo();
			}
	}
	HANDLE handle;
	handle=CreateFile(_T(".//测试结果.html"),GENERIC_WRITE,0,NULL,CREATE_ALWAYS,FILE_ATTRIBUTE_NORMAL,NULL);
	if(INVALID_HANDLE_VALUE!= handle ) 
	{
		DWORD Num; 
		CString str;
		str = _T("该串口被打开啦！");
		::WriteFile(handle,str,strlen(str),&Num,NULL);
		::CloseHandle(handle); 
	}
	if(i==0)	
	{
		flagECIComReceiveStatus=0;	//表示刚打开的时候,Com1刚开始接收数据
		ECIComReceiveString=_T("");	//初始化接收的string
		m_strRXDataCom1 = _T("");	
	}
}








bool OpenCom(UINT i,CWnd *pPortOwner)			//打开第i个串口，其中i=ECICOM或者TBCOM。当i=ECICOM时，指的是与ECIBox连接的串口；当i=TBCOM时，指的是与测试工装连接串口
{
	BOOL bComSuccess = FALSE;	//COM1打开成功
	ComPortInfo portInfo;
	UINT portnr;

	if((i!=ECICOM)&&(i!=TBCOM))
	{
		MessageBox(0,"试图打开未定义的串口号，请打开与ECI连接的串口或者与测试工装连接的串口！\n","警告",0);
		return false;
	}

	while(!bComSuccess)			//除非COM1都打开了，否则就一直处理
	{
		//获取串口信息
		portnr = GetPortInformation(i,portInfo);

		//如果没有获得串口号,则弹出对话框表示需要配置串口，再弹出配置对话框
		if(portnr==-1)			
		{
			 CString str;
			 str = _T("与ECIBox连接的串口尚未配置，请配置串口！");
			 AfxMessageBox(str);
			 return false;
			 //弹出配置窗口,以便进行串口信息配置！
			// OnBnClickedInfo();	 
		}

		if(m_ComPort[i].InitPort(pPortOwner ,portInfo.portnr,portInfo.com_baudrate,portInfo.com_parity,portInfo.com_databits,portInfo.com_stopbits,EV_RXFLAG|EV_RXCHAR,portInfo.com_writeBufferSize))//初始化成功
		{
			m_ComPort[i].StartMonitoring();                       //启动串口监视线程
			CString str;
			if(i==ECICOM)		 MessageBox(0,"连接ECI的串口打开成功！","提示",0);
			if(i==TBCOM)		 MessageBox(0,"连接测试工装的串口打开成功！","提示",0);
			bComSuccess = true;
		}
		else                                                                                                                                                                                                                                                                                          //初始化失败
		{
			CString str;
			str.Format( _T("COM%d没有发现，或被其他设备占用！COM%d 打开失败！该串口应该与ECIBox连接！") ,portnr,portnr);
			bComSuccess = false;
		}
	}
}
}


m.count(k);		//returns the number of occurrences of k within m.
m.find(k);		//returns an iterator to the element indexed by k,
				//if there is one ,or returns an off-the-end iterator if the key is not present.

Using count to determine whether a Key is in the map.
count effectively indicates whether the key is present.
The return from count is more useful for multimaps.


int occurs = 0;
if(word_count.count("football"))
	occurs = word_count["football"];

-------------------------------------------------------------------


/*A program to transform words.
* Takes two arguments: 
* The first is name of the word transfomation file 
* The sencond is name of the input to transform
*/
#include "stdafx"
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(int argc, char **argv)
{
	// map to hold the word transformation pairsL
	// key is the word to look for in the input;
	// value is word to use in the output
	map<string,string> trans_map;
	string key,value;
	if(argc!=3)
		throw runtime_error("wrong number of arguments");
	ifstream map_file;
	if(!open_file(map_file,argv[1]))
		throw runtime_error("no transfomation file!");
	while(map_file>>key>>value)
		trans_map.insert(make_pair(key,value));
	//Ok now we're ready to transformations
	//open the input file and check that open succeeded

	ifstream input;
	if(!open_file(input,argv[2]))
		throw runtime_error("no input file!");
	string line;		//hold each line from the input
	//read the text to transform it a line at a time
	while(geline(input,line))
	{
		istringstream stream(line);
		string word;
		bool firstword = true;	//controls whether a space is printed
		while(stream>>word)
		{
			map<string,string>::const_iterator map_it = trans_map.find(word);
			if(map_it!=tran_map.end())
				word = map_it->sencond;
			if(firstword)
				firstword = false;
			else
				cout<<" ";
			cout<<word;
		}
		cout<<endl;
	}
	return 0;
}

