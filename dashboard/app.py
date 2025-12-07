import psutil
from flask import Flask, render_template

app = Flask(__name__)

def get_service_status(service_name):
    """Check if Windows service is running."""
    try:
        service = psutil.win_service_get(service_name)
        return service.status() == 'running'
    except:
        return False

@app.route('/')
def home():
    # 1. Retrieve the system stats
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('C://').percent
    
    # 2. Check Services stats
    # we use 'ssh_status' here to match what is inside index.html
    ssh_status = get_service_status('sshd') 
    nas_status = get_service_status('FileBrowserService')
        
    return render_template('index.html', 
                           cpu=cpu, 
                           ram=ram, 
                           disk=disk, 
                           ssh_status=ssh_status,  # Fixed name to match HTML
                           nas_status=nas_status)
  
# !!! THIS MUST BE UN-INDENTED (Touch the left side) !!!
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)