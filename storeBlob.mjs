import fs from 'fs'
import { NFTStorage, Blob } from 'nft.storage'
import { argv } from 'node:process';
import { env } from 'node:process';

const endpoint = 'https://api.nft.storage' // the default
const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDM3MmU3MTYxNzVkODM3MUM0OTYxY2M2OEE4ZDlDNWNDMGQxOTEyNDIiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTYzNDc1MTA3NTM1NCwibmFtZSI6IkRCZHVtcCJ9.fANErEAfKOTP-9Szjjo2tI7QWhuY5fPO8ZtDZ30WMzk' // your API key from https://nft.storage/manage

async function main() {
  const storage = new NFTStorage({ endpoint, token })
  const data = await fs.promises.readFile(process.argv[2])
  const cid = await storage.storeBlob(new Blob([data]))
  console.log({ cid })
  const status = await storage.status(cid)
  console.log(status)
}
main()
