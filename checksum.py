      public byte[] CreateTxArray(byte command, int data1)
        {
            byte[] cmdByte = { command };
            byte[] checkSum = new byte[1];
            byte[] byteArrayTemp = BitConverter.GetBytes(data1);
            int[] byteArray1 = { byteArrayTemp[0] };
            byte[] outputBytes = new byte[3]; //cmdByte.Length + byteArray1.Length + checkSum.Length];

            Buffer.BlockCopy(cmdByte, 0, outputBytes, 0, cmdByte.Length);
            Buffer.BlockCopy(byteArray1, 0, outputBytes, cmdByte.Length, byteArray1.Length);

            checkSum = CalculateCheckSum(outputBytes, outputBytes.Length);
            byte nByte = BitConverter.GetBytes(outputBytes.Length)[0];
            outputBytes[outputBytes.Length - 1] = checkSum[0];

            return outputBytes;
        }
