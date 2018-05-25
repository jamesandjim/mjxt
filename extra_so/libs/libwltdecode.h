#ifndef libwltdecode_h
#define libwltdecode_h

extern "C"
{
/**
*	@file		libwltdecode.h
*	@brief		身份证照片解码库
*	@author		scar.chen@zkteco.com
*	@date		2016-04-07
*	@version	1.0
*	@par	版权：
*				ZKTeco
*	@par	历史版本
*			NULL
*	@note		
*
*/


/**
	*	@brief	解析身份证照片到内存
	*	@param	:
	*	参数说明如下表
	*	name			|	type		  |	param direction		|	description of param
	*	----------------|-----------------|---------------------|------------------------
	*	wltData			| unsigned char*  |	[in]				|	1024字节wlt图像数据
	*	imageData		| unsigned char*  |	[out]				|	输出bmp图像二进制数据（内存大小必须>(102*3+2)*126）
	*	cbImageData		| int			  |	[in]				|	imageData内存大小
	*	@return
	*		1： 成功
	*		其他：失败
	*	@note 
*/
int wlt2bmpBuffer(unsigned char* wltData, unsigned char* imageData, int cbImageData)


};

#endif
