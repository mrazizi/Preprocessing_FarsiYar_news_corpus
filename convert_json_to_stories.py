import json

# input json pathes
farsnews_json_path = "json_files/farsnews.json"
yjc_json_path = "json_files/yjc.json"

# output story folder pathes
farsnews_stories_folder = "stories/farsnews"
yjc_stories_folder = "stories/yjc"





def process_data_line(line, output_file_name, folder_path, yjc=False):
    """
    This functions gets a line and does the following:
        - Parses line as a json object
        - Extracts news summary and news body
        - splits news body by \n
        - saves news body and summary in the following format
            
            '''
            [news body line 1]

            [news body line 2]

            @highlight
            [news summary]
            '''
    """

    line_json = json.loads(line)

    if yjc:
        news_summary = line_json['Summary']
        news_body = line_json['Body']
    else:
        news_summary = line_json['NewsSummary']
        news_body = line_json['NewsBody']

    output_text = ""

    # spliting news_body by line
    news_body_lines_split = news_body.split("\n")
    

    # appending each news body line to output text
    for l in news_body_lines_split:
        output_text += l 
        output_text += "\n\n"

    # appending news summary to output text
    output_text += "@highlight"
    output_text += "\n\n"
    output_text += news_summary
    output_text += "\n\n"
    

    # write to file
    complete_output_file_name = folder_path + "/" + str(output_file_name) + ".story"
    f = open(complete_output_file_name, "w")
    f.write(output_text)
    f.close()

        
########### Preprocess FarsNews ###########
files_count = 0
json_line_count = 0

print(f"*************************[FarsNews]*************************")

with open(farsnews_json_path, encoding='utf-8-sig') as fp:
    line = fp.readline()

    try:
        process_data_line(line, files_count, farsnews_stories_folder)
        files_count += 1
    except Exception as e:
        print(e)
        print(f"[LOG] line {json_line_count} skipped!")
    
    json_line_count += 1


    while line:
        line = fp.readline()

        try:
            process_data_line(line, files_count, farsnews_stories_folder)
            files_count += 1
        except Exception as e:
            # print(e)
            # print(f"[LOG] line {json_line_count} skipped!")
            continue
        
        json_line_count += 1


        if json_line_count % 100 == 0:
            print(f"[LOG] json line {json_line_count} processed!")



########### Preprocess YJC ###########
files_count = 0
json_line_count = 0

print(f"*************************[YJC]*************************")

with open(yjc_json_path, encoding='utf-8-sig') as fp:
    line = fp.readline()

    try:
        process_data_line(line, files_count, yjc_stories_folder, True)
        files_count += 1
    except Exception as e:
        print(e)
        print(f"[LOG] line {json_line_count} skipped!")
    
    json_line_count += 1


    while line:
        line = fp.readline()

        try:
            process_data_line(line, files_count, yjc_stories_folder, True)
            files_count += 1
        except Exception as e:
            # print(e)
            # print(f"[LOG] line {json_line_count} skipped!")
            continue
        
        json_line_count += 1


        if json_line_count % 100 == 0:
            print(f"[LOG] json line {json_line_count} processed!")