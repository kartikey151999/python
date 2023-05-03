import re
def chk_specialChar(self,string):
    special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (special_char.search(string) == None):
        return False
    else:
        return True
class BasePasswordManager:
    old_passwords=['pass','pass12']
    def get_password(self):
       return self.old_passwords[-1]
    def is_correct(self,str):
      val=True if self.get_password()==str else False;
      return val
ob1=BasePasswordManager()
class PasswordManager(BasePasswordManager):
  newpass = input("Enter the newpassword :")
  def set_password(self,newpass):
    if ob2.get_level(ob2.newpass)>ob2.get_level(ob2.get_password()) and len(ob2.newpass)>=6:
        print('change sucessfull')
        ob2.old_passwords[-1]=ob2.newpass
        return ob2.old_passwords[-1]
    else:
        print('change unsucessfull')
        return ob2.old_passwords[-1]
  def get_level(self,*argv):
     for arg in argv:
        if(arg.isalpha() or arg.isnumeric()):
          level=0
        elif (arg.isalnum()):
          level=1
        else:
          level=2
     return level
ob2=PasswordManager()
print(f'Current password is {ob2.get_password()} and level is :',ob2.get_level(ob2.get_password()))
print(f'new password is {ob2.newpass} and level is :',ob2.get_level(ob2.newpass))
print(ob2.set_password(ob2.newpass))

