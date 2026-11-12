"""Run reproducible built-in demonstration checks from this folder."""
import json
from rule90 import run as r90
from lumpability import run as lump
from nested_worlds import run as nest
from finite_state import run as finite

def main():
    results={'rule90':r90(),'lumpability':lump(),'nested':nest(),'finite_state':finite()}
    print(json.dumps({'status':'PASS','tests':results},ensure_ascii=False,indent=2))
    return results

if __name__=='__main__':main()
