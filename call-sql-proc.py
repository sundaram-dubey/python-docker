import mysql.connector
from mysql.connector import Error

''' sql proc query
DELIMITER //
CREATE PROCEDURE getTemplates (ctr VARCHAR(50))
BEGIN
 SELECT * FROM templates WHERE rill_job_id=ctr;
END //
DELIMITER ;
'''

## this is for mysql
try:
    connection = mysql.connector.connect(host='host.docker.internal', ## host used inside docker, for runnig file separately use localhost
                                         database='Klaxon', ## database name
                                         user='sundaram',
                                         password='Sonu@123',
                                         auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    cursor.callproc('getTemplates', ["ec9c88bc-6b5a-4309-b41f-52fa8db2bc87"])
    # print results
    print("template details - ")
    for result in cursor.stored_results():
        print(result.fetchall())

except mysql.connector.Error as error:
    print("Failed to execute stored procedure: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")