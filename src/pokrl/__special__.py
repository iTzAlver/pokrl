# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                                                           #
#   This file was created by: Alberto Palomo Alonso         #
# Universidad de Alcalá - Escuela Politécnica Superior      #
#                                                           #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
import os
__version__ = '0.1.0'
# Get the current directory:
__abs_path__ = os.path.abspath(__file__)
__src_path__ = os.path.dirname(__abs_path__)
# Set the environment variables:
os.environ['PY_SA_SRC'] = __src_path__
os.environ['PY_SA_VER'] = __version__
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                        END OF FILE                        #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
