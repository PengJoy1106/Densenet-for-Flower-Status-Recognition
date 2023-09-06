# coding:gbk

import os
import torch
from PIL import Image
from torchvision import transforms



from densenet.model import densenet121


def predict(img_path):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    data_transform = transforms.Compose(
        [transforms.Resize(256),
         transforms.CenterCrop(224),
         transforms.ToTensor(),
         transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    assert os.path.exists(img_path), "file: '{}' dose not exist.".format(img_path)
    img = Image.open(img_path)
    # plt.imshow(img)
    # [N, C, H, W]
    img = data_transform(img)
    # expand batch dimension
    img = torch.unsqueeze(img, dim=0)

    # # read class_indict
    # json_path = './class_indices.json'
    # assert os.path.exists(json_path), "file: '{}' dose not exist.".format(json_path)
    #
    # with open(json_path, "r") as f:
    #     class_indict = json.load(f)

    # classes = {'0': '��ǰ���ܹ���ʩ����ҩ���뼰ʱ����~', '1': '�¶�̫���������Ļ����챻ɹ����~', '2': 'ȱˮ�������»���ʾ���ڵ�״̬���Ƿǳ���~', '3': 'Ӫ�����������벹��Ӫ��~', '4': '�¶ȹ��ͣ����Ļ����춳����~'}
    classes = {'0': '���Ļ����⵽ϸ�����ֺ����������뾡�����~', '1': '���Ļ����⵽������ֺ����������뾡�����~', '2': '���Ļ�������溦���������뾡�����~', '3': '���Ļ����⵽�������ֺ����������뾡�����~'}

    # create model
    model = densenet121(num_classes=4).to(device)
    # load model weights
    model_weight_path = "C:/Users/Pengyk/Desktop/Densenet for Flower Status Recognition/results/Infectious_Diseases_Results/best.pth"
    model.load_state_dict(torch.load(model_weight_path, map_location=device))
    model.eval()

    with torch.no_grad():
        # predict class
        output = torch.squeeze(model(img.to(device))).cpu()
        predict = torch.softmax(output, dim=0)
        predict_cla = torch.argmax(predict).numpy()

    # return classes[str(predict_cla)]

    print_res = "{}  ׼ȷ��: {:.3}".format(classes[str(predict_cla)],
                                                 predict[predict_cla].numpy())
    return(print_res)


if __name__ == '__main__':
    # load image
    img_path = "datasets/Infectious Diseases/Fungal Damage/3.JPG"
    result = predict(img_path)
    print(result)
