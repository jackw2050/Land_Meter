import binascii
#  public byte[] CalculateCheckSum(byte[] intBytes, int numBytes)
#         {
#             var checkSum = 0;
#             // byte[] intBytes = BitConverter.GetBytes(data);
#             Array.Resize(ref intBytes, numBytes);
#             byte[] txCmd = new byte[1 + intBytes.Length + 1];

#             Buffer.BlockCopy(intBytes, 0, txCmd, 1, intBytes.Length);

#             // Concatenate array1 and array2.

#             //  txCmd[0] = cmd;
#             for (int i = 0; i < numBytes; i++)
#             {
#                 checkSum = checkSum ^ txCmd[i];
#             }
#             txCmd[txCmd.Length - 1] = BitConverter.GetBytes(checkSum)[0]; ;


#             return BitConverter.GetBytes(checkSum);

#         }






def makeTXcmd(cmd, array):
    # Byte    Function
    # 0       Number of bytes to follow
    # 1       Command ID
    # 2       Data
    # N       Last data byte
    # N+1     Check sum (EOR of bytes 2 - N)
    myByteArray = array
    checksum = calculateChecksum(myByteArray)
    myByteArray.insert(0,cmd)
    myByteArray.insert(0,len(myByteArray))
    myByteArray.append(checksum) 
    
    print  binascii.hexlify(bytearray(myByteArray))
    return myByteArray
    
    
    
    
def calculateChecksum(cmdArray):
    checksum = 0
    # checksum = hex(sum(bytearray(cmdArray)))
    for index in cmdArray:
        checksum = checksum ^ index
    print checksum
    return checksum
    
    
command = 0x1B

myByteArray = [0xFF, 0xFF]
# outputBytes = binascii.hexlify(bytearray(myByteArray))
# myByteArray.insert(0,command)
# outputBytes = binascii.hexlify(bytearray(myByteArray))
# checksum = hex(sum(bytearray(myByteArray)))
# print outputBytes, checksum
print makeTXcmd(command, myByteArray)
