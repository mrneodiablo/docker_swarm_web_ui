from django.conf.urls import url
from .views import DashBoard
from .node_views import Nodes
from .container_views import Containers
from .image_views import Images
from .volume_views import Volumes
from .network_views import Networks
from .user_views import LoginUser, ManagerUser
from .logs_views import ManagerLogs
from .registry_views import ManagerRegistry
from .product_views import Products
from .error_views import Error
 


dashboard = DashBoard()
container = Containers()
nodes = Nodes()
images = Images()
volumes = Volumes()
networks = Networks()
login = LoginUser()
user = ManagerUser()
logs = ManagerLogs()
registry = ManagerRegistry()
product = Products()
error = Error()

urlpatterns = [
    ################### index ########################
    url(r'^$', dashboard.index, name='DashBoard'),

    ################### logs #########################
    url(r'^logs$', logs.board, name='LogsBoard'),

    ################### user  ########################
    url(r'^user$', user.board, name='UserBoard'),
    url(r'^user/create$', user.create, name='UserCreate'),
    url(r'^user/(?P<username>[a-zA-Z0-9_-]+)$$', user.update, name='UserDetail'),
    ################### login ########################
    url(r'^login$', login.login, name='LoginBoard'),
    url(r'^logout$', login.logout, name='LogoutBoard'),

    #################### container ################### 
    url(r'^containers$', container.board, name='ContainerBoard'), 
    url(r'^containers/create$', container.create, name='ContainerCreate'),
    url(r'^containers/monitor/(?P<containerid>[a-zA-Z0-9_-]+)$', container.monitor, name='ContainerMonitor'),
    url(r'^containers/start/(?P<containerid>[a-zA-Z0-9_-]+)$', container.start, name='ContainerStart'),
    url(r'^containers/stop/(?P<containerid>[a-zA-Z0-9_-]+)$', container.stop, name='ContainerStop'),
    url(r'^containers/kill/(?P<containerid>[a-zA-Z0-9_-]+)$', container.kill, name='ContainerKill'),
    url(r'^containers/pause/(?P<containerid>[a-zA-Z0-9_-]+)$', container.pause, name='ContainerPause'),
    url(r'^containers/unpause/(?P<containerid>[a-zA-Z0-9_-]+)$', container.unpause, name='ContainerUnPause'),
    url(r'^containers/restart/(?P<containerid>[a-zA-Z0-9_-]+)$', container.restart, name='ContainerRestart'),
    url(r'^containers/scale$', container.scale, name='ContainerScale'),   
    url(r'^containers/remove$', container.remove, name='ContainerRemove'),  
    url(r'^containers/rename$', container.rename, name='ContainerRename'),  
    url(r'^containers/create$', container.create, name='ContainerCreate'),
    url(r'^containers/(?P<containerid>[a-zA-Z0-9_-]+)$', container.detail, name='ContainerDetail'),
    url(r'^containers/chart/(?P<containerid>[a-zA-Z0-9_-]+)$', container.chart, name='ContainerChart'),

    ###########h######### node #######################
    url(r'^node$', nodes.board, name='NodeBoard'),
    url(r'^node/api/getcpunode$', nodes.apiGetCpuNode),     
    url(r'^node/(?P<host>[a-z0-9A-Z_-]+)$', nodes.detail, name='NodeDetail'), 

    ################### images ######################
    url(r'^images$', images.board, name='ImagesBoard'),
    url(r'^images/pull$', images.pull, name='ImagesPull'),
    url(r'^images/tag$', images.tag, name='ImagesTag'),
    url(r'^images/(?P<images_id>[a-z0-9A-Z_-]+)$', images.detail, name='ImagesDetail'),
    
    ################### volumes ######################
    url(r'^volumes$', volumes.board, name='VolumesBoard'),
    url(r'^volumes/create$', volumes.create, name='VolumesCreate'),

    ################### networks ######################
    url(r'^networks$', networks.board, name='NetworksBoard'),
    url(r'^networks/create$', networks.create, name='NetworksCreate'),
    url(r'^networks/connect$', networks.connect, name='NetworksConnect'),
    url(r'^networks/disconnect$', networks.disconnect, name='NetworksDisconnect'),
    url(r'^networks/api/getnetwork$', networks.apiGetNetwork),
    url(r'^networks/api/listvlan$', networks.apiListVlan),
    url(r'^networks/(?P<network_id>[a-z0-9A-Z_-]+)$', networks.detail, name='NetworksDetail'),

    ################### registry ######################
    url(r'^registry$', registry.board, name='RegistryBoard'),
    url(r'^registry/api/listrepo$', registry.apiListImages),
    url(r'^registry/(?P<name_registry>[a-zA-Z0-9_-]+)$', registry.detail, name='RegistryDetail'),

    ################### product ######################
    url(r'^product$', product.board, name='ProductBoard'),
    url(r'^product/api/inpsect$', product.apiInspect,),

    ####################################error#####################
    url(r'^deny$', error.permissionDeny, name='PermissionDeny'),

]
