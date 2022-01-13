Repo for Master's theses: Desenvolvimento da técnica Private Information Retrieval (PIR$^2$LWE) para garantir a privacidade de carteiras leves em um ambiente de blockchain.

The scripts simulate Bob, a lightweight client, using PIR2LWE instead of Bloom Filters to recover a block (instead of the Bloom Paths) to calculate the hash related with the transaction.
The simulation uses Pyfhel lib with rlwe to encript a group of blocks, homomorphic multiplication to remove all the blocks which Bob is not interested and return the reponse with the content of the block desired.

1- Run the script "pir2lwe_bob_req". That's script is going to create the cryptosystem parameters in the folders configured and create a request to Alice (normal node).<br>
2- Run the script "pir2lwe_alice". All the block's content in the script are encrypted with Bob's pk and a homorphic multiplication is applied. The reponse is sent back to Bob (simulate by creating files in folders).<br>
3- Run the script "pir2lwe_bob_resp". Using the response, the script decypher the content and return the blocked request by Bob.<br>