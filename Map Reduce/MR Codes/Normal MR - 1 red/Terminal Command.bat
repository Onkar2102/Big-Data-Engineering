cd /home/mayank0953
mkdir wordcount
cd wordcount
vi WordCount.java


# Compile the Java code
javac -cp $(hadoop classpath) WordCount.java

# Verify the class files were created
ls -l WordCount*.class

# Create the JAR file
jar cf wc.jar WordCount*.class

# Verify the JAR was created
ls -l wc.jar


# Create input directory in HDFS
hadoop fs -mkdir -p /user/mayank0953/input

# go to the cluster root folder
cd ..
cd ~
pwd
# pwd should give a address like /home/{cluster_name}
mkdir localFile
cd localFile/
pwd

# creating dbzinput.txt
vi dbzinput.txt
cat dbzinput.txt
# Goku Vegeta Gohan
# Goku Frieza Goku
# Vegeta Goku Gohan Frieza
# Gohan Frieza Goku Goku



# Copy your input files to HDFS
hadoop fs -put ~/localFile/F /user/mayank0953/input/
hadoop fs -put ~/localFile/logfile.txt /user/mayank0953/input/

# Verify files are in HDFS
hadoop fs -ls /user/mayank0953/input/


# before running following command for the jar related, make sure u r in the correct directory
ls
# this will show .txt file in localFile
cd ..
# this will show dir like localFile and wordcount
cd wordcount/
ls
# here, wc.jar will be present

# For dbzinput.txt
hadoop jar wc.jar WordCount /user/mayank0953/input/dbzinput.txt /user/mayank0953/output_dbz
hadoop fs -ls /user/mayank0953/output_dbz

# View results
hadoop fs -cat /user/mayank0953/output_dbz/part-r-00000

# For logfile.txt
hadoop jar wc.jar WordCount /user/mayank0953/input/logfile.txt /user/mayank0953/output_log

# View results
hadoop fs -cat /user/mayank0953/output_log/part-r-00000


Goku Vegeta Gohan
Goku Frieza Goku
Vegeta Goku Gohan Frieza
Gohan Frieza Goku Goku