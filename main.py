import fastapi as _fastapi
import blockchain as _blockchain

blockchain = _blockchain.Blockchain()

app = _fastapi.FastAPI()


# endpoint to mine a block
@app.post('/mine_block')
def mine_block(data: str):
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail='Blockchain is invalid'
        )
    
    return blockchain.mine_block(data=data)

# endpoint to return an entire blockchain
@app.get('/blockchain/')
def get_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail='Blockchain is invalid'            
        )
    
    return blockchain.chain

# endpoint to check if blockchain is valid
@app.get('/validate/')
def is_blockchain_valid():
    return blockchain.is_chain_valid()

# endpoint that returns the previous block
@app.get("/previous_block/")
def get_previous_block():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail='Blockchain is invalid'            
        )
    
    return blockchain.get_previous_block()