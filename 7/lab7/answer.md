# Encryption and Decryption
1. Decrypt `file1.txt.gpg` with the password `ofcdecal` (*for real-life purposes, never store passwords in plaintext*). What are the decrypted contents of `file1.txt.gpg`?
> ```bash
> gpg --decrypt file1.txt.gpg
> # type "ocfdecal" in the prompt
> # Output:
> # gpg: AES.CFB encrypted data
> # gpg: encrypted with 1 passphrase
> # Quack
> ```

2. What command allows you to import a key?
> Use `gpg --import <key-file>` to import a public key.

3. What command allows you to export a key to a file? (Add the `--armor` flag to ASCII-encode the key so it can be sent easily in text form)
> Use `gpg --export <key-id> > <key-file>` to export a public key.

4. What command allows you to see all of the keys on your keyring?
> Use `gpg --list-keys` to list all keys on your keyring.

5. Use the private key lab7privkey to decrypt the file file2.txt.gpg (for real-life purposes, it is necessary to keep private keys secret). What are the decrypted contents of b8/file2.txt.gpg?
> The content is "Woof".

# Hashing (Checksums)
1. What is the MD5 hash of the file `file3.txt`?
> ddbefc9c1d8a8d9195a420a7181352e9 

2. What is the SHA1 hash of the MD5 hash of `file3.txt`? In other words, what is `SHA1(MD5(file3.txt))`?
> `echo -n $(md5sum file3.txt | awk '{print $1}') | sha1sum` and you will get `e9f61163d7265caa71877eb8e76726f906f6cfeb`.

# File Security
Run sudo setup.sh before beginning this section.

1. `file4.txt`: What are the permissions of this file? Explain what they allow and disallow.
> -rwxrwxrwx 1 root root   15 Mar 15  2023 file4.txt

2. `file5`: Make this file executable and execute it. What is its printout?
> aching flair.

3. `file6.txt`: Change this file to be under your ownership. What command did you use?
> `sudo chown yourusername:yourusername file6.txt`

4. `file7.txt`: Make this file readable only to you. What command did you use?
> `sudo chmod 400 file7.txt`

5. `file8.txt`: Change this file’s permissions such that only root should be able to read this file and no one should be able to edit it. What command did you use?
> `sudo chmod 400 file8.txt`, `sudo chown root:root file8.txt`.

6. `file9.txt`: Choose any method to make this file readable to you and unreadable to the previous owner. What command did you use?
>`sudo chown yourusername:yourusername file9.txt`, `chmod 400 file9.txt`.