# Example report

```
{
  "installation": {
    "timeline": [
      {
        "action": "uninstalled",
        "timestamp": "07/04/2022 13:59:34",
        "path": "C:\\Users\\win1user\\AppData\\Roaming\\AnyDesk"
      },
      {
        "action": "installed",
        "timestamp": "07/04/2022 13:59:45",
        "path": "C:\\Users\\win1user\\AppData\\Roaming\\AnyDesk"
      }
    ],
    "is_installed": true,
    "installation_path": "C:\\Users\\win1user\\AppData\\Roaming\\AnyDesk",
    "rda_id": "207966795"
  },
  "connections": [
    {
      "no": 0,
      "remote_ip": "145.100.107.226:49670",
      "connection_start": "2022-04-07 22:57:32",
      "connection_end": "2022-04-07 22:57:59",
      "remote_user": "win1user",
      "remote_rda_id": "944018568",
      "remote_os": "Windows,",
      "remote_version": "7.0.6"
    },
    {
      "no": 1,
      "remote_ip": "145.100.107.227:49673",
      "connection_start": "2022-04-07 23:07:16",
      "connection_end": "2022-04-07 23:07:44",
      "remote_user": "win3user",
      "remote_rda_id": "943208521",
      "remote_os": "Windows,",
      "remote_version": "7.0.6"
    },
    {
      "no": 2,
      "remote_ip": "145.100.107.227:49673",
      "connection_start": "2022-04-07 23:24:46",
      "connection_end": "2022-04-07 23:25:05",
      "remote_user": "win3user",
      "remote_rda_id": "943208521",
      "remote_os": "Windows,",
      "remote_version": "7.0.6"
    }
  ],
  "file trace": [
    {
      "connection_no": 0,
      "drives": {
        "C:": [
          {
            "file_path": "C:\\Users\\win1user\\AppData\\Roaming\\AnyDesk\\user.conf",
            "reason": "Data truncation"
          },
          {
            "file_path": "C:\\Users\\win1user\\AppData\\Roaming\\AnyDesk\\user.conf",
            "reason": "Data extend | Data truncation"
          },
          {
            "file_path": "C:\\Users\\win1user\\AppData\\Roaming\\AnyDesk\\user.conf",
            "reason": "Data extend | Data truncation | Close"
          },
          {
            "file_path": "C:\\Users\\win1user\\AppData\\Roaming\\AnyDesk\\user.conf",
            "reason": "Data truncation"
          },

          ...
          
		  {
            "file_path": "C:\\\\Windows\\Prefetch\\AgGlUAD_S-1-5-21-406305298-2519373244-2512540256-1001.db",
            "reason": "Data extend | Data truncation | Close"
          },
          {
            "file_path": "C:\\\\Windows\\Prefetch\\AgGlUAD_P_S-1-5-21-406305298-2519373244-2512540256-1001.db",
            "reason": "Data truncation"
          },
          {
            "file_path": "C:\\\\Windows\\Prefetch\\AgGlUAD_P_S-1-5-21-406305298-2519373244-2512540256-1001.db",
            "reason": "Data extend | Data truncation"
          },
          {
            "file_path": "C:\\\\Windows\\Prefetch\\AgGlUAD_P_S-1-5-21-406305298-2519373244-2512540256-1001.db",
            "reason": "Data extend | Data truncation | Close"
          }
        ]
      }
    },
    {
      "connection_no": 1,
      "drives": {
        "C:": [
          {
            "file_path": "C:\\Windows\\SysWOW64\\config\\systemprofile\\AppData\\Local\\Microsoft\\Windows\\Explorer\\iconcache_idx.db",
            "reason": "Data overwrite | Close"
          },
          {
            "file_path": "C:\\Windows\\SysWOW64\\config\\systemprofile\\AppData\\Local\\Microsoft\\Windows\\Explorer\\iconcache_16.db",
            "reason": "Data overwrite | Close"
          },
          {
            "file_path": "C:\\Users\\win1user\\AppData\\Roaming\\AnyDesk\\user.conf",
            "reason": "Data truncation"
          },
          {
            "file_path": "C:\\Users\\win1user\\AppData\\Roaming\\AnyDesk\\user.conf",
            "reason": "Data extend | Data truncation"
          },

          ...

          {
            "file_path": "C:\\\\Windows\\Prefetch\\SEARCHPROTOCOLHOST.EXE-0CB8CADE.pf",
            "reason": "Data extend | Data truncation"
          },
          {
            "file_path": "C:\\\\Windows\\Prefetch\\SEARCHPROTOCOLHOST.EXE-0CB8CADE.pf",
            "reason": "Data extend | Data truncation | Close"
          },
          {
            "file_path": "C:\\\\Windows\\Prefetch\\SEARCHFILTERHOST.EXE-77482212.pf",
            "reason": "Data truncation"
          },
          {
            "file_path": "C:\\\\Windows\\Prefetch\\SEARCHFILTERHOST.EXE-77482212.pf",
            "reason": "Data extend | Data truncation"
          },
          {
            "file_path": "C:\\\\Windows\\Prefetch\\SEARCHFILTERHOST.EXE-77482212.pf",
            "reason": "Data extend | Data truncation | Close"
          }
        ]
      }
    },
    {
      "connection_no": 2,
      "drives": {
        "C:": [
          {
            "file_path": "C:\\ProgramData\\AnyDesk\\ad_svc.trace",
            "reason": "Data extend"
          },
          {
            "file_path": "C:\\Users\\win1user\\AppData\\Roaming\\AnyDesk\\user.conf",
            "reason": "Data truncation"
          },
          {
            "file_path": "C:\\Users\\win1user\\AppData\\Roaming\\AnyDesk\\user.conf",
            "reason": "Data extend | Data truncation"
          },
          {
            "file_path": "C:\\Users\\win1user\\AppData\\Roaming\\AnyDesk\\user.conf",
            "reason": "Data extend | Data truncation | Close"
          },
          
		  ...

          {
            "file_path": "C:\\ProgramData\\AnyDesk\\service.conf",
            "reason": "Data truncation"
          },
          {
            "file_path": "C:\\ProgramData\\AnyDesk\\service.conf",
            "reason": "Data extend | Data truncation"
          },
          {
            "file_path": "C:\\ProgramData\\AnyDesk\\service.conf",
            "reason": "Data extend | Data truncation | Close"
          }
        ]
      }
    }
  ],
  "program trace": [
    {
      "connection_no": 0,
      "prefetch_data": [
        {
          "timestamp": "07/04/2022 22:57:43",
          "executable": "AUDIODG.EXE",
          "location_hash": "BDFD3029"
        },
        {
          "timestamp": "07/04/2022 22:57:43",
          "executable": "AUDIODG.EXE",
          "location_hash": "BDFD3029"
        },
        {
          "timestamp": "07/04/2022 22:57:43",
          "executable": "AUDIODG.EXE",
          "location_hash": "BDFD3029"
        }
      ],
      "timeline_data": []
    },
    {
      "connection_no": 1,
      "prefetch_data": [
        {
          "timestamp": "07/04/2022 23:07:27",
          "executable": "AUDIODG.EXE",
          "location_hash": "BDFD3029"
        },
        {
          "timestamp": "07/04/2022 23:07:27",
          "executable": "AUDIODG.EXE",
          "location_hash": "BDFD3029"
        },
        {
          "timestamp": "07/04/2022 23:07:27",
          "executable": "AUDIODG.EXE",
          "location_hash": "BDFD3029"
        },
        {
          "timestamp": "07/04/2022 23:07:38",
          "executable": "NOTEPAD.EXE",
          "location_hash": "D8414F97"
        },
        {
          "timestamp": "07/04/2022 23:07:38",
          "executable": "NOTEPAD.EXE",
          "location_hash": "D8414F97"
        },
        {
          "timestamp": "07/04/2022 23:07:38",
          "executable": "NOTEPAD.EXE",
          "location_hash": "D8414F97"
        },
        {
          "timestamp": "07/04/2022 23:07:42",
          "executable": "SEARCHPROTOCOLHOST.EXE",
          "location_hash": "0CB8CADE"
        },
        {
          "timestamp": "07/04/2022 23:07:42",
          "executable": "SEARCHPROTOCOLHOST.EXE",
          "location_hash": "0CB8CADE"
        },
        {
          "timestamp": "07/04/2022 23:07:42",
          "executable": "SEARCHPROTOCOLHOST.EXE",
          "location_hash": "0CB8CADE"
        },
        {
          "timestamp": "07/04/2022 23:07:42",
          "executable": "SEARCHFILTERHOST.EXE",
          "location_hash": "77482212"
        },
        {
          "timestamp": "07/04/2022 23:07:42",
          "executable": "SEARCHFILTERHOST.EXE",
          "location_hash": "77482212"
        },
        {
          "timestamp": "07/04/2022 23:07:42",
          "executable": "SEARCHFILTERHOST.EXE",
          "location_hash": "77482212"
        }
      ],
      "timeline_data": [
        {
          "Id": 216949657299826199645308043503088393263,
          "AppId": "[{\"application\":\"{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\\\\notepad.exe\",\"platform\":\"windows_win32\"},{\"application\":\"{D65231B0-B2F1-4857-A4CE-A8E7C6EA7D27}\\\\notepad.exe\",\"platform\":\"windows_win32\"},{\"application\":\"{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\\\\notepad.exe\",\"platform\":\"packageId\"},{\"application\":\"\",\"platform\":\"alternateId\"}]",
          "PackageIdHash": "eUssiHYOx8gt4grLn60pEG2m1QnscYA3695n7jpHJwY=",
          "AppActivityId": "ECB32AF3-1440-4086-94E3-5311F97F89C4\\{ThisPCDesktopFolder}\\hello_there.txt",
          "ActivityType": 5,
          "ActivityStatus": 1,
          "ParentActivityId": 0,
          "Tag": null,
          "Group": null,
          "MatchId": null,
          "LastModifiedTime": "2022-04-07 23:07:32",
          "ExpirationTime": "2022-05-07 23:07:32",
          "Payload": 950879233406526873269303658073594773208859118918415330377922767365893816142960757648647788614258828525335600735499784059187169515187110123909337261602914790033553371645399623291489902266751026184538143362469437719746264137463367073990657508036866104845916237252823706990738900375002443878102547575599623687961868926152266850054266494866409902859634208148407401974265530710530277885350008767294101843292066763244778891654418025389121040567682519162018343020288428047026968881498692862472528550598763679829721075701490844807243433347159290934402900752645340757508142701867744778675858324690122515636134222228005158462629585642623526368275871139078358829944598154426400797046485271814707089079207219151347306047252231559267245186310227229882457067027291612624188512156671357845762501037080708411059867273928065134418721491392354857664940111309769706990094796467041401811508473067606310064113140865729228003970800100772279778272477837608809525015255416429081504588413,
          "Priority": 1,
          "IsLocalOnly": 0,
          "PlatformDeviceId": "dBbwzQBKL4EbVMxl5+c1mrsz16b3hopBqZmKj+SxUjU=",
          "DdsDeviceId": null,
          "CreatedInCloud": 0,
          "StartTime": "2022-04-07 23:07:32",
          "EndTime": "1970-01-01 01:00:00",
          "LastModifiedOnClient": "2022-04-07 23:07:32",
          "GroupAppActivityId": "",
          "ClipboardPayload": null,
          "EnterpriseId": "",
          "OriginalPayload": null,
          "UserActionState": 0,
          "IsRead": 0,
          "OriginalLastModifiedOnClient": null,
          "GroupItems": "",
          "LocalExpirationTime": 0,
          "ETag": 4813
        },
        {
          "Id": 265319290114503061643750721673773774520,
          "AppId": "[{\"application\":\"{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\\\\notepad.exe\",\"platform\":\"windows_win32\"},{\"application\":\"{D65231B0-B2F1-4857-A4CE-A8E7C6EA7D27}\\\\notepad.exe\",\"platform\":\"windows_win32\"},{\"application\":\"{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\\\\notepad.exe\",\"platform\":\"packageId\"},{\"application\":\"\",\"platform\":\"alternateId\"}]",
          "PackageIdHash": "eUssiHYOx8gt4grLn60pEG2m1QnscYA3695n7jpHJwY=",
          "AppActivityId": "ECB32AF3-1440-4086-94E3-5311F97F89C4\\{ThisPCDesktopFolder}\\hello_there.txt",
          "ActivityType": 6,
          "ActivityStatus": 1,
          "ParentActivityId": 0,
          "Tag": null,
          "Group": null,
          "MatchId": null,
          "LastModifiedTime": "2022-04-07 23:07:32",
          "ExpirationTime": "2022-05-07 23:07:38",
          "Payload": 1159346999520307639746200089195203563870105519834957923516152884383668785542613931487713527478873777526620407203831151683202232829102571468814002506640295569878602878691274184767635637237722400182815900770034374918776257027808369723848200339365540348382918913953491813805593629738877689988088638282321516351367003268650885026603797128283443240348644886503716712324395194354541080338481654957280644669068594724803216765764807783425320195964931010533874151109501565,
          "Priority": 1,
          "IsLocalOnly": 0,
          "PlatformDeviceId": "dBbwzQBKL4EbVMxl5+c1mrsz16b3hopBqZmKj+SxUjU=",
          "DdsDeviceId": null,
          "CreatedInCloud": 0,
          "StartTime": "2022-04-07 23:07:31",
          "EndTime": "2022-04-07 23:07:38",
          "LastModifiedOnClient": "2022-04-07 23:07:38",
          "GroupAppActivityId": "",
          "ClipboardPayload": null,
          "EnterpriseId": "",
          "OriginalPayload": null,
          "UserActionState": 0,
          "IsRead": 0,
          "OriginalLastModifiedOnClient": null,
          "GroupItems": "",
          "LocalExpirationTime": 0,
          "ETag": 4820
        }
      ]
    },
    {
      "connection_no": 2,
      "prefetch_data": [
        {
          "timestamp": "07/04/2022 23:24:47",
          "executable": "SPPSVC.EXE",
          "location_hash": "B0F8131B"
        },
        {
          "timestamp": "07/04/2022 23:24:47",
          "executable": "SPPSVC.EXE",
          "location_hash": "B0F8131B"
        },
        {
          "timestamp": "07/04/2022 23:24:47",
          "executable": "SPPSVC.EXE",
          "location_hash": "B0F8131B"
        },
        {
          "timestamp": "07/04/2022 23:24:57",
          "executable": "ANYDESK.EXE",
          "location_hash": "7E87D21F"
        },
        {
          "timestamp": "07/04/2022 23:24:57",
          "executable": "ANYDESK.EXE",
          "location_hash": "7E87D21F"
        },
        {
          "timestamp": "07/04/2022 23:24:57",
          "executable": "ANYDESK.EXE",
          "location_hash": "7E87D21F"
        },
        {
          "timestamp": "07/04/2022 23:24:57",
          "executable": "AUDIODG.EXE",
          "location_hash": "BDFD3029"
        },
        {
          "timestamp": "07/04/2022 23:24:57",
          "executable": "AUDIODG.EXE",
          "location_hash": "BDFD3029"
        },
        {
          "timestamp": "07/04/2022 23:24:57",
          "executable": "AUDIODG.EXE",
          "location_hash": "BDFD3029"
        }
      ],
      "timeline_data": []
    }
  ]
}
```