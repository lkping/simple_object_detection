#coding:utf-8
import PIL.Image as Image
import os

#需要安装Pillow：pip install pillow

#图片压缩批处理  
def compressImage(srcPath,dstPath):  
    for filename in os.listdir(srcPath):  
        #如果不存在目的目录则创建一个，保持层级结构
        if not os.path.exists(dstPath):
                os.makedirs(dstPath)        

        #拼接完整的文件或文件夹路径
        srcFile=os.path.join(srcPath,filename)
        dstFile=os.path.join(dstPath,filename)
        print(srcFile)
        print(dstFile)

        #如果是文件就处理
        if os.path.isfile(srcFile):     
            #打开原图片缩小后保存，可以用if srcFile.endswith(".jpg")或者split，splitext等函数等针对特定文件压缩
            sImg=Image.open(srcFile)  
            w,h=sImg.size  
            print(w,h)

            dImg=sImg.resize((int(w/10),int(h/10)),Image.ANTIALIAS)  #设置压缩尺寸和选项，注意尺寸要用括号
            dImg.save(dstFile) #也可以用srcFile原路径保存,或者更改后缀保存，save这个函数后面可以加压缩编码选项JPEG之类的
            print(dstFile+" compressed succeeded")

        #如果是文件夹就递归
        if os.path.isdir(srcFile):
            compressImage(srcFile,dstFile)

if __name__=='__main__':  
    compressImage("./images","./images_output")