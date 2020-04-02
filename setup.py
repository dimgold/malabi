import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='malabi',  
     version='0.1',
     scripts=['malabi'] ,
     author="Dima Goldeberg",
     author_email="dimgold@gmail.com",
     description="ML BI tools",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/dimgold/malabir",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
