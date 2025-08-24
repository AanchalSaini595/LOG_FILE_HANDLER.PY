import os
def read_file(user_input):
   if not os.path.exists(user_input):
    return []
   with open(user_input,'r') as file:
      return [ line.strip() for line in file]
def Extract_data(user_input):
    if not os.path.isfile(user_input):
     print("File does not exists")
    if os.path.getsize(user_input) == 0:
     print("File is empty....")
    else:
     ips=[]
     errors=[]
     with open(user_input,'r') as file:
       for texts in file:
        if "-" in texts:
          parts = texts.split("-",1)
          ips.append(parts[0].strip())
          errors.append(parts[1].strip())
    with open("ips.txt", "w") as ip_file:
        for ip in ips:
            ip_file.write(ip + "\n")
        freq_ip(ips)
    # Save Errors
    with open("errors.txt", "w") as err_file:
        for error in errors:
            
            err_file.write(error + "\n")
        freq_error(errors)   
    print("✅ Data saved to ips.txt and errors.txt")
def freq_ip(ips):
   max_count_ip = max(ips.count(ip) for ip in ips)  
def freq_error(errors):
   max_count_error = max(errors.count(error) for error in errors)
   print(max_count_error)              
def main():
  user_input = input("Enter the file path the you want to analyze: ")
  read_file(user_input)
  Extract_data(user_input)
if __name__ == "__main__":
    main()
