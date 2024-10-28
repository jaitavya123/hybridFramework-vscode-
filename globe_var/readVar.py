from configparser import ConfigParser, NoSectionError, NoOptionError


def var1(key,value):
 try:  
  pull_var = ConfigParser()
  pull_var.read('C:/Users/LENOVO/VScodeProjects/autoTest/globe_var/var.ini')
  print("--------->",pull_var.get(key,value))

  return pull_var.get(key,value)
 
 except Exception as e:
  print("----->Exception in readVAr.py file ",e) 
 except FileNotFoundError:
  print("-----> Configuration file not found. Please check the file path.")
 except NoSectionError:
  print(f"-----> The section '{key}' was not found in the configuration file.")
 except NoOptionError:
  print(f"-----> The option '{value}' was not found under the section '{key}'.")  


#var1("DOMAIN","url")