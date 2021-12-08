import sys,os
import xlwt

path = sys.argv[1] #provid directory path of all proteom sequence files (Single fasta sequence is needed within single file)
dirr = os.listdir(path)

book = xlwt.Workbook()
sheet1 = book.add_sheet("AA_comp_stat", cell_overwrite_ok=True)
row = sheet1.row(0)
row.write(0,"File_name")    
 
    


def acomp(seq,i,fil):
	aa = "ARNDCQEGHILKMFPSTWYV"
	row = sheet1.row(i)
	row.write(0,fil)
	for a in aa:
		#print a,"=",seq.count(a)
		row = sheet1.row(i)
		row.write(aa.find(a)+1,seq.count(a))
	

	for a in aa:
		row = sheet1.row(0)
		row.write(aa.find(a)+1,a)



i=1
for fil in dirr:
	FIL=open(path+'/'+fil,'r')
	hline=FIL.readline()
	seq = FIL.read()
	acomp(seq,i,fil)
	i=i+1
	FIL.close()
	#if i == 65534:break


book.save("test1.xls")