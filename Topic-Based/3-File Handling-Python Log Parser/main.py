def parsed_logs(line):
    return line.strip()
    return line.strip().split(maxsplit=1)

# with open("./test.txt") as input_file, open("./output.txt", "w") as output_file:
#     # lines = file.readlines()

#     errors = [line for line in input_file if "ERROR" in line] #Filter error logs
#     # print(errors)
#     transformed_logs = map(parsed_logs, errors) # Transform each line of log
#     # print(transformed_logs)

#     for line in transformed_logs:
#         output_file.write(line + " \n")

# # print(lines)


with open("./test.txt") as input_file, open("./output.txt", "w") as output_file:
    error_logs = filter(lambda line: "ERROR" in line, input_file)
    transformed_logs = map(lambda line: line.strip(), error_logs)

    for line in transformed_logs:
        output_file.write(line + " \n")