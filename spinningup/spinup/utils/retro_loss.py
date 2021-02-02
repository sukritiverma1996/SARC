import torch
import torch.nn as nn

# Util for retro loss
'''
def retr_loss(y, y_p, y_gt, K, gamma, p, func, scaled):
    if gamma is None:
        gamma = K/(K+1)
    if p == 1:
        if func == 'l1':
            loss_val = nn.L1Loss()(y, y_gt) - gamma*nn.L1Loss()(y, y_p.detach())
        elif func == 'mse':
            loss_val = (y - y_gt).pow(2).mean() - gamma*(y-y_p.detach()).pow(2).mean()
        elif func == 'l2':
            loss_val = torch.sqrt(nn.MSELoss()(y, y_gt)) - gamma*torch.sqrt(nn.MSELoss()(y, y_p.detach()))
    elif p == 2:
        if func == 'l1':
            a, b = nn.L1Loss()(y, y_p.detach()), nn.L1Loss()(y, y_gt)
        elif func == 'mse':
            b, a = (y - y_gt).pow(2).mean(), (y-y_p.detach()).pow(2).mean()
        elif func == 'l2':
            a, b = torch.sqrt(nn.MSELoss()(y, y_p.detach())), torch.sqrt(nn.MSELoss()(y, y_gt))
            
        loss_val = b - gamma*(a**2) - gamma*(b**2) - 2*a*b*gamma
    
    ## scaling the retrospective loss magnitude
    if scaled:
        loss_val = (K+1)*loss_val
    
    return loss_val

def retr_loss(y, y_p, y_gt, K, gamma, p, func, scaled):
    if gamma is None:
        gamma = K/(K+1)
    if func == 'l1':
        loss_val1 = nn.L1Loss()(y, y_gt) - gamma*nn.L1Loss()(y, y_p.detach())
    elif func == 'mse':
        loss_val1 = (y - y_gt).pow(2).mean() - gamma*(y-y_p.detach()).pow(2).mean()
    elif func == 'l2':
        loss_val1 = torch.sqrt(nn.MSELoss()(y, y_gt)) - gamma*torch.sqrt(nn.MSELoss()(y, y_p.detach()))
    if func == 'l1':
        a, b = nn.L1Loss()(y, y_p.detach()), nn.L1Loss()(y, y_gt)
    elif func == 'mse':
        b, a = (y - y_gt).pow(2).mean(), (y-y_p.detach()).pow(2).mean()
    elif func == 'l2':
        a, b = torch.sqrt(nn.MSELoss()(y, y_p.detach())), torch.sqrt(nn.MSELoss()(y, y_gt))

    loss_val2 = b - gamma*(a**2) - gamma*(b**2) - 2*a*b*gamma

    loss_val = torch.clamp(loss_val1, min=0) #+ torch.clamp(loss_val2, min=0)
    ## scaling the retrospective loss magnitude
    if scaled:
        loss_val = (K+1)*loss_val

    return loss_val
'''

def retro_loss(y, y_p, y_gt, K, scaled, L=1):
    a = nn.L1Loss()(y, y_gt)
    b = nn.L1Loss()(y, y_p.detach())
    c = nn.L1Loss()(y_gt, y_p.detach())
    #loss_val = K * (2*a - b + c)
    gamma = K/(K+L)
    loss_val = (a - gamma*b + gamma*c)
    if scaled:
        loss_val *= (K+L)
    return loss_val
