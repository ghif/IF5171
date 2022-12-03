from torch import nn

class SoftmaxClassifier(nn.Module):
    def __init__(self, d_in=28*28, d_out=10):
        super(SoftmaxClassifier, self).__init__()
        self.flatten = nn.Flatten()
        self.network = nn.Sequential(
            nn.Linear(d_in, d_out)
        )
        
    def forward(self, x):
        x = self.flatten(x)
        logits = self.network(x)
        return logits
    
class MLP(nn.Module):
    def __init__(self, d_in=28*28, d_out=10):
        super(MLP, self).__init__()
        self.flatten = nn.Flatten()
        self.network = nn.Sequential(
            nn.Linear(d_in, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, d_out)
        )
        
    def forward(self, x):
        x = self.flatten(x)
        logits = self.network(x)
        return logits
    
class MLPAutoEnc(nn.Module):
    def __init__(self, d_in=28*28, d_z=100, d_h=512):
        super(MLPAutoEnc, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(d_in, d_h),
            nn.ReLU(),
            nn.Linear(d_h, d_z)
        )
        
        self.decoder = nn.Sequential(
            nn.Linear(d_z, d_h),
            nn.ReLU(),
            nn.Linear(d_h, d_in),
            nn.Sigmoid()
        )
        
    def forward(self, x):
        z = self.encoder(x)
        xr = self.decoder(z)
        return xr
    
class AutoEncSigm(nn.Module):
    def __init__(self, d_in=28*28, d_z=100, d_h=512):
        super(AutoEncSigm, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(d_in, d_h),
            nn.ReLU(),
            nn.Linear(d_h, d_z),
            nn.Sigmoid()
        )
        
        self.decoder = nn.Sequential(
            nn.Linear(d_z, d_h),
            nn.ReLU(),
            nn.Linear(d_h, d_in),
            nn.Sigmoid()
        )
        
    def forward(self, x):
        z = self.encoder(x)
        xr = self.decoder(z)
        return xr
    
class AutoEncFMNIST(nn.Module):
    def __init__(self, d_in=28*28, d_z=100, d_h=512):
        super(AutoEncFMNIST, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(d_in, d_h),
            nn.ReLU(),
            nn.Linear(d_h, d_z),
            nn.Sigmoid()
        )
        
        self.decoder = nn.Sequential(
            nn.Linear(d_z, d_h),
            nn.ReLU(),
            nn.Linear(d_h, d_in),
            nn.Sigmoid()
        )
        
    def forward(self, x):
        z = self.encoder(x)
        xr = self.decoder(z)
        return xr
    
class VAE(nn.Module):
    def __init__(self, d_in=28*28, d_z=100, d_h=512):
        super(VAE, self).__init__()
        
        self.d_z = d_z
        
        self.encoder = nn.Sequential(
            nn.Linear(d_in, d_h),
            nn.ReLU(),
            nn.Linear(d_h, d_z * 2),
        )
        
        self.decoder = nn.Sequential(
            nn.Linear(d_z, d_h),
            nn.ReLU(),
            nn.Linear(d_h, d_in),
            nn.Sigmoid()
        )
        
    def reparameterise(self, mu, logvar):
        if self.training:
            std = logvar.mul(0.5).exp_()
            eps = std.new_empty(std.size()).normal_()
            return eps.mul_(std).add_(mu)
        else:
            return mu
    
    def encode(self, x):
        mu_logvar = self.encoder(x)
        mu_logvar = mu_logvar.reshape(-1, 2, self.d_z)
        mu = mu_logvar[:, 0, :]
        logvar = mu_logvar[:, 1, :]
        z = self.reparameterise(mu, logvar)
        return z, mu, logvar
    
    def decode(self, z):
        return self.decoder(z)
        
    def forward(self, x):
        z, mu, logvar = self.encode(x)
        xr = self.decode(z)
        return xr, mu, logvar
        
class ConvNet(nn.Module):
    def __init__(self, d_out=10):
        super(ConvNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1,out_channels=32,kernel_size=3)
        self.conv2 = nn.Conv2d(in_channels=32,out_channels=32,kernel_size=3)
        self.max_pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        
        self.conv3 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3)
        self.conv4 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3)
        self.max_pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        
        self.fc1 = nn.Linear(1024, 128)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(128, d_out)
        
    # Progresses data across layers    
    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.max_pool1(out)
        
        out = self.conv3(out)
        out = self.conv4(out)
        out = self.max_pool2(out)
                
        out = out.reshape(out.size(0), -1)
        
        out = self.fc1(out)
        out = self.relu1(out)
        out = self.fc2(out)
        return out
    
class ConvNetSVHN(nn.Module):
    def __init__(self, d_out=10, c=3):
        super(ConvNetSVHN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=c,out_channels=32,kernel_size=3)
        self.conv2 = nn.Conv2d(in_channels=32,out_channels=32,kernel_size=3)
        self.max_pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        self.conv3 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3)
        self.conv4 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3)
        self.max_pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        self.fc1 = nn.Linear(1600, 512)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(512, d_out)
        
    # Progresses data across layers    
    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.max_pool1(out)
        
        out = self.conv3(out)
        out = self.conv4(out)
        out = self.max_pool2(out)
                
        out = out.reshape(out.size(0), -1)
        
        out = self.fc1(out)
        out = self.relu1(out)
        out = self.fc2(out)
        return out
    
class ConvNetCIFAR(nn.Module):
    def __init__(self, d_out=100, c=3):
        super(ConvNetCIFAR, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=c,out_channels=32,kernel_size=3)
        self.bn1 = nn.BatchNorm2d(num_features=32)
        
        self.conv2 = nn.Conv2d(in_channels=32,out_channels=64,kernel_size=3)
        self.bn2 = nn.BatchNorm2d(num_features=64)
        
        self.max_pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3)
        self.bn3 = nn.BatchNorm2d(num_features=128)
        
        self.conv4 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3)
        self.bn4 = nn.BatchNorm2d(num_features=256, affine=True)
        
        self.max_pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        self.fc1 = nn.Linear(6400, 1024)
        self.bn5 = nn.BatchNorm1d(num_features=1024)        
        self.relu1 = nn.ReLU()
        
        self.fc2 = nn.Linear(1024, d_out)
        
    # Progresses data across layers    
    def forward(self, x):
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu1(out)
        
        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu1(out)
        
        out = self.max_pool1(out)
        
        out = self.conv3(out)
        out = self.bn3(out)
        out = self.relu1(out)
        
        out = self.conv4(out)
        out = self.bn4(out)
        out = self.relu1(out)
        
        out = self.max_pool2(out)
        

        out = out.reshape(out.size(0), -1)
        
        out = self.fc1(out)
        out = self.bn5(out)
        out = self.relu1(out)
        
        out = self.fc2(out)
        return out
    
    
class ConvNetCIFAR_v2(nn.Module):
    def __init__(self, d_out=100, c=3):
        super(ConvNetCIFAR_v2, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=c,out_channels=32,kernel_size=3)
        
        self.conv2 = nn.Conv2d(in_channels=32,out_channels=64,kernel_size=3)
        
        self.max_pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3)
        
        self.conv4 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3)
        
        self.max_pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        self.fc1 = nn.Linear(6400, 1024)

        self.fc2 = nn.Linear(1024, d_out)

        self.relu = nn.ReLU()
        self.do2d = nn.Dropout2d(0.25)
        self.do1d = nn.Dropout(0.25)
        
    # Progresses data across layers    
    def forward(self, x):
        out = self.conv1(x)
        out = self.relu(out)
        
        out = self.do2d(out)
        out = self.conv2(out)
        out = self.relu(out)
        
        out = self.max_pool1(out)
        
        out = self.do2d(out)
        out = self.conv3(out)
        out = self.relu(out)

        out = self.do2d(out)
        out = self.conv4(out)
        out = self.relu(out)
        
        out = self.max_pool2(out)
        

        out = out.reshape(out.size(0), -1)
        
        out = self.do1d(out)
        
        out = self.fc1(out)
        out = self.relu(out)
        
        out = self.do1d(out)
        out = self.fc2(out)
        return out
    
class ConvNetCIFAR_v3(nn.Module):
    def __init__(self, d_out=100, c=3):
        super(ConvNetCIFAR_v3, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=c,out_channels=32,kernel_size=3)
        
        self.conv2 = nn.Conv2d(in_channels=32,out_channels=64,kernel_size=3)
        self.bn2d1 = nn.BatchNorm2d(64, affine=False)
        
        self.max_pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3)
        self.conv4 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3)
        self.bn2d2 = nn.BatchNorm2d(256, affine=False)
        self.max_pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        self.fc1 = nn.Linear(6400, 1024)
        self.bn1d1 = nn.BatchNorm1d(1024, affine=False)
        
        self.fc2 = nn.Linear(1024, d_out)

        self.relu = nn.ReLU()
        
    # Progresses data across layers    
    def forward(self, x):
        out = self.conv1(x)
        
        out = self.conv2(out)
        out = self.bn2d1(out)
        out = self.relu(out)
        
        out = self.max_pool1(out)
        
        out = self.conv3(out)
        
        out = self.conv4(out)
        out = self.bn2d2(out)
        out = self.relu(out)
        
        out = self.max_pool2(out)
        
        out = out.reshape(out.size(0), -1)
        
        out = self.fc1(out)
        out = self.bn1d1(out)
        out = self.relu(out)
        
        out = self.fc2(out)
        return out