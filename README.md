# AWS-Logs-Parser

The assumptions for the given task:
1. As per the given task, only support for version 2 logs is developed and any other format logs will be skipped.
2. One more assumption is that, the value for dstport is in the 6th index, i.e., it is the 7th value and the value for protocol is in the 7th index, i.e., it is the 8th value in the given logs.
3. Also, only the dstport and protocol values from the logs are utilized, which are the seventh and eighth fields in the log data.
4. Only a list of most frequently used protocols were used, namely, icmp, igmp, tcp, udp, ipv6, rsvp, gre, esp, ah, icmpv6, eigrp, ospf, ipip, sctp, were used for mapping and all other protocols come under unknown.
5. The combinations which are mentioned in the lookup_table txt mappings are only considered and all other combinations are mentioned as unnamed.
6. As there was a restriction regarding the installation of libraries, flask was not used, which could have helped with uploading the flow_logs and lookup_table files, rather than placing them manually in the execution folder.
7. No other external libraries were utilized for the full process workflow.
8. As it was not possible to simulate a full length test where the log file is around 10 MB, a considerably long logs file was tested.
9. As there was no file names or naming conventions mentioned for the code as well as the output, most appropriate names were chosen and used.
10. As there were no specific messages to be shown when file is not found or unable to be read, all commonly used messages were structured and displayed.
11. As the matches should be case insensitive, regardless of the protocol being in uppercase or lowercase, the mappings will be checked for.
12. As there was no mention in the requirement stating that the tags should be considered to be case insensitive, the tags were considered exactly as mentioned in the lookup file.


Tests Implemented:
1. From manually calculatable values to large sized data, all types of values were passed to the code and the output was compared.
2. The check if the files are missing or if the files are corrupted, if the corresponding is displayed, was cross verified.
3. Time for execution if the log data is very large was checked, to ensure the efficiency is up to the point, even if immense data is processed.
4. Checks were made to ensure that if the log data is not in the expected version format, with some fields which are required are missing or misarranged, those log entries are skipped.
5. Checks were made to ensure that if certain fields are missing in the logs for some entries, resulting in data type mismatch or vallue mismatch, those entries are skipped 
6. Checks were made to check if the parser works fine if the lookup_table does not have any mappings, with only headings, the output mentions all are unnamed and also, the prot/protocol combination is listed though.
7. If both the logs as well as the mappings do not have any meaningful entries, then it was checked if the output file did not have any entries.
8. In addition to this, all the file related tests, value related tests and outputs were verified.
9. Values in both lower and uppercases were passed for protocol to ensure the matches were evaluated properly, to make sure they are case insensitive.

Execution Steps:
1. Load the lookup data into the lookup_table.txt file and place it in the same folder as the python script, parser.py file.
2. Load the log data into the flow_logs.txt file and place it in the same folder as the python script, parser.py file.
3. After updating the files, now run the python script, parser.py.
4. Check the output in the output.txt file, in the format requested in the description.
