from flask import Flask, jsonify, request
import json

product =[{}]

app = Flask(__name__)


@app.route('/',methods=["GET"])
def index():   
    return "<h1> Ola Dev</>"

  
@app.route('/produtos',methods=["GET"])
def produto():
  
    return jsonify(product)


@app.route('/produtos',methods=["POST"])
def produtoAdd():
  
    product.append(request.get_json())
    return jsonify(product), 201


@app.route('/produtos/<int:id>',methods=["DELETE"])
def produtoDel(id):
    index = id
    try:
      del product[index]
      return jsonify(product)
    except:
      return jsonify({'error':'not found'}), 404

@app.route('/produtos/<int:id>',methods=["PUT"])
def produtoUpdate(id):
    index = id
    try:
      for prod in product:
        if prod["codigo"] == index:
          prod.update(request.get_json())
          return jsonify(product)
      
    except:
      return jsonify({'error':'not found'}), 404

@app.route('/dinheiro',methods=["GET"])
def dinheiro():
    
    valor ={'valor':0}
    return jsonify(valor)


@app.route('/cartao',methods=["GET"])
def cartao():
    
    valor ={'valor':0}
    return jsonify(valor)

if __name__ =='__main__':
    app.run()
