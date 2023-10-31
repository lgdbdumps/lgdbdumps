import fs from 'fs'
import { NFTStorage, Blob } from 'nft.storage'
import { argv } from 'node:process';
import { env } from 'node:process';

const endpoint = 'https://api.nft.storage' // the default
const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGFBRTU0NTE5Yzc4NTkwMEM2OEM4QmU2RkQ5MjRDNTFDOGY0NzAzRWYiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY5ODc3ODkxODQ4NywibmFtZSI6ImpwZ3MifQ.l5yZJz-A-XtovzM8HbMPWZ2QP97P9CK5ZYMT7axwJ2A' // your API key from https://nft.storage/manage

async function main() {
  const storage = new NFTStorage({ endpoint, token })
  const data = await fs.promises.readFile(process.argv[2])
  const cid = await storage.storeBlob(new Blob([data]))
  console.log({ cid })
  const status = await storage.status(cid)
  console.log(status)
}
main()
