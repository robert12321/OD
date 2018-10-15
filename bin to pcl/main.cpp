#include<fstream>
#include<stdint.h>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<string>
int main()
{
	// allocate 4 MB buffer (only ~130*4*4 KB are needed)
	int32_t num = 1000000;
	float *data = (float*)malloc(num*sizeof(float));

	// pointers
	float *px = data+0;
	float *py = data+1;
	float *pz = data+2;
	float *pr = data+3;
	
	std::string filenameBinIn = "1.bin";
	std::string filenameBinOut = "binarka.bin";
	
	
	// load point cloud
	FILE *stream;
	stream = fopen (filenameBinIn.c_str(),"rb");
	num = fread(data,sizeof(float),num,stream)/4;
	fclose(stream);
	for (int32_t i=0; i<num; i++) {
		std::cout<<*px<<" "<<*py<<" "<<*pz<<" "<<*pr<<std::endl;
		px+=4; py+=4; pz+=4; pr+=4;
	}

	// saving point cloud to binary
	stream = fopen (filenameBinOut.c_str(),"wb");
  	fwrite(data,sizeof(float),4*num,stream);
	fclose(stream);

	// free memory
	free(data);
	return 0;
}
