#ifndef __INTERFACE_H__
#define __INTERFACE_H__

#ifdef __cplusplus
extern "C"
{
#endif
int ZKID_OpenPort(int iPort);
int ZKID_ClosePort(int iPort);
int ZKID_OpenPortEx(const char * dev);

int ZKID_GetSAMStatus(int iPort,int bIfOpen);
int ZKID_ResetSAM(int iPort,int bIfOpen);
int ZKID_GetSAMIDToStr(int iPort,char *pcSAMID,int iIfOpen);
int ZKID_GetSAMID(int iPort,unsigned char *pucSAMID,int iIfOpen);

int ZKID_StartFindIDCard(int iPort,unsigned char *pucIIN,int bIfOpen);

int ZKID_GetCOMBaud(int iPort,unsigned int  *puiBaud);
int ZKID_SetCOMBaud(int iPort,unsigned int  uiCurrBaud,unsigned int  uiSetBaud);

int ZKID_SetMaxRFByte(int iPort,unsigned char ucByte,int bIfOpen);

int ZKID_SelectIDCard(int iPort,unsigned char *pucSN,int bIfOpen);

int ZKID_ReadBaseMsg(int iPort,unsigned char * pucCHMsg,unsigned int *	puiCHMsgLen,unsigned char * pucPHMsg,unsigned int  *puiPHMsgLen,int bIfOpen);
int ZKID_ReadBaseFPMsg(int iPort,unsigned char *pucCHMsg,unsigned int *puiCHMsgLen,unsigned char *pucPHMsg,unsigned int *puiPHMsgLen,unsigned char *pucFPMsg,unsigned int *puiFPMsgLen,int bIfOpen);
int ZKID_ReadNewAppMsg(int iPort, unsigned char *pucAppMsg, unsigned int *puiAppMsgLen, int iIfOpen);
int ZKID_ReadCardMsgSN(int iPort, unsigned char *pucMsgSN, int iIfOpen);
int ZKID_PHunpack(char *src, char *dst);

int ZKID_MFInit(int iPort);
int ZKID_Mifare_REQA(unsigned char mode);
int ZKID_SetBaudRate(unsigned int baud);
int ZKID_Mifare_AnticollA(unsigned int *CardNumber);
int ZKID_Mifare_SelectA(unsigned int uid);
int ZKID_Mifare_GetSerNum(unsigned char *SerNum);
int ZKID_Mifare_SetSerNum(unsigned char *SerNum);
int ZKID_Mifare_HaltA();
int ZKID_Mifare_Read(unsigned char addr, unsigned char blocks, unsigned char *key,unsigned char auth,unsigned char mode,unsigned char *buf,unsigned int * uid);
int ZKID_Mifare_Write(unsigned char addr,unsigned char blocks,unsigned char *key,unsigned char auth, unsigned char mode,unsigned char * buf, unsigned int * uid, int protect);
int ZKID_Mifare_Get_SNR(unsigned char mode,unsigned char halt,unsigned char *serialnumber);
int ZKID_Mifare_Get_SNR_SFZ(unsigned char mode,unsigned char halt,unsigned char *serialnumber);
void ZKID_Mifare_Perror(int errno);
#ifdef __cplusplus
}
#endif

#endif
