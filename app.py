from flask import Flask

FAI=Flask(__name__)

@FAI.route('/wish')
def wish():
    return 'i love u '

@FAI.route('/love')
def love():
    return 'i will marry u'

if __name__=='__main__':
      
      FAI.run(debug=True)