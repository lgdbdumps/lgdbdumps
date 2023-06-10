import fs from 'fs'
import { NFTStorage, Blob } from 'nft.storage'
import { argv } from 'node:process';
import { env } from 'node:process';

const endpoint = 'https://api.nft.storage' // the default
const token = process.env.NFT_APIKEY // your API key from https://nft.storage/manage

async function main() {
  const storage = new NFTStorage({ endpoint, token })
  const data = await fs.promises.readFile(process.argv[2])
  const cid = await storage.storeBlob(new Blob([data]))
  console.log({ cid })
  const status = await storage.status(cid)
  console.log(status)
}
main()
