rm -f endusers.response endusers.csv 
java -cp ./classes:./lib/saaj-api.jar:./lib/saaj-impl.jar:./lib/mail.jar:./lib/activation.jar:./lib/jaxm-api.jar:./lib/jaxm-runtime.jar:./lib/xercesImpl.jar:./lib/xml-apis.jar AxlSqlToolkit -username=administrator -password=ciscopsdt -host=10.10.20.1 -input=endusers.xml -output=endusers.response
python xmltocsv.py endusers.response endusers.csv