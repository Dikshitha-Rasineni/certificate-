# Certificate page — permanent link + QR

The page always lives at the same URL. Until `certificate.pdf` exists the page is
completely blank; once you add the PDF, the same URL (and the same QR) shows only
the PDF.

## 1. Publish the site (once)
1. Create a new GitHub repo (e.g. `certificate`) and upload these files:
   `index.html`, `vercel.json`, `README.md`, `make_qr.py`.
2. On vercel.com → **Add New → Project** → import that repo → **Deploy**
   (no build settings needed — it's a plain static site).
3. Your permanent URL is `https://<project-name>.vercel.app`.
   Open it: you should see a blank white page.

## 2. Make the QR code (once)
```
pip install qrcode[pil]
python make_qr.py https://<project-name>.vercel.app
```
This creates `certificate-qr.png` and `certificate-qr.svg`. Print/share these.

## 3. Add the certificate (later)
1. Rename your file to exactly **`certificate.pdf`**.
2. Upload it to the root of the same GitHub repo (Add file → Upload files → Commit).
3. Vercel redeploys automatically in ~30 seconds. Scan the QR — the PDF shows.

To replace it later, upload a new file with the same name. The QR stays the same.

## Keep the QR working forever
- Don't delete or rename the Vercel project (that changes the URL).
- Don't change the file name `certificate.pdf` (or update `PDF_FILE` in `index.html` to match).
