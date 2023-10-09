#!/usr/bin/python
# python 3.x

import zipfile, plistlib, sys, re


qx = {
    "NSLocationAlwaysUsageDescription":"始终访问地理位置权限",
    "NSLocationWhenInUseUsageDescription":"在使用期间访问地理位置权限",
    "NSContactsUsageDescription":"访问通讯录",
    "NSCalendarsUsageDescription":"读取、创建日历信息",
    "NSRemindersUsageDescription":"访问注意事项权限",
    "NSPhotoLibraryUsageDescription":"获取相册",
    "NSPhotoLibraryAdditionsUsageDescription":"获取媒体资料库",
    "NSMicrophoneUsageDescription":"通过麦克风录音或进行语音输入",
    "NSSpeechRecognitionUsageDescription":"语音识别会将录音发送给Apple 以处理语音识别请求",
    "NSCameraUsageDescription":"访问相机权限",
    "NSMotionUsageDescription":"健康数据",
    "NSHealthUpdateUsageDescription":"健康更新",
    "NSHealthShareUsageDescription":"健康分享",
    #####################
    "Location Always Usage Description":"始终访问地理位置权限",
    "Location When InUse Usage Description":"在使用期间访问地理位置权限",
    "Contacts Usage Description":"访问通讯录",
    "Calendars Usage Description":"读取、创建日历信息",
    "Reminders Usage Description":"访问注意事项权限",
    "Photo Library Usage Description":"获取相册",
    "Photo Library Additions Usage Description":"获取媒体资料库",
    "Microphone Usage Description":"通过麦克风录音或进行语音输入",
    "Speech Recognition Usage Description":"语音识别会将录音发送给Apple 以处理语音识别请求",
    "Camera Usage Description":"访问相机权限",
    "Motion Usage Description":"健康数据",
    "Health Update Usage Description":"健康更新",
    "Health Share Usage Description":"健康分享"

}

def analyze_ipa_with_plistlib(ipa_path):
    ipa_file = zipfile.ZipFile(ipa_path)
    plist_path = find_plist_path(ipa_file)
    plist_data = ipa_file.read(plist_path)
    plist_root = plistlib.loads(plist_data)
    print_ipa_info(plist_root)
    
    
def print_ipa_info(plist_root):
    print ('Display Name: %s' % plist_root['CFBundleName'])
    print ('Bundle Identifier: %s' % plist_root['CFBundleIdentifier'])
    print ('Version: %s' % plist_root['CFBundleShortVersionString'])
    No = 1
    for key in plist_root:
        if key in qx or key[:2]=='NS':
            try:
                print(str(No)+'-'*5+key+'-'*10+qx[key])
                #print(str(No)+'-'*5+key+'-'*10+str(plist_root[key]))
                #print(plist_root[key])
            except:
                print(str(No)+'-'*5+key+'-'*10+str(plist_root[key]))
            No += 1
    #print(plist_root)

def find_plist_path(zip_file):
    name_list = zip_file.namelist()
    #print(name_list)
    pattern = re.compile(r'Payload/[^/]*.app/Info.plist')
    for path in name_list:
        m = pattern.match(path)
        if m is not None:
            return m.group()

if __name__ == '__main__':
    args = sys.argv[1:]
    #args = ['EmoaIPhone_LH.ipa']
    
    try:
        ipa_path = args[0]
        analyze_ipa_with_plistlib(ipa_path)
    except:
        print ('Usage: python '+sys.argv[0]+' /path/to/ipa')
        print('Example: python '+sys.argv[0]+' example.ipa')
        exit(0)
