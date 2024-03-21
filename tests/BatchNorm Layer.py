OK_FORMAT = True

test = {   'name': 'BatchNorm Layer',
    'points': 0,
    'suites': [   {   'cases': [   {   'code': '>>> list(BatchNorm2d(2)(torch.zeros((3,2,7,6))).shape) == [3,2,7,6]\nTrue',
                                       'failure_message': 'Shape Test Failed',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0,
                                       'success_message': 'Shape Test Passed'},
                                   {   'code': '>>> type(BatchNorm2d(2)(torch.zeros((3,2,7,6)))) == torch.Tensor\nTrue',
                                       'failure_message': 'Type Test Failed',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0,
                                       'success_message': 'Type Test Passed'},
                                   {   'code': ">>> hasattr(BatchNorm2d(2), 'gamma') and hasattr(BatchNorm2d(2), 'beta')\nTrue",
                                       'failure_message': 'Param Name Test Failed',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0,
                                       'success_message': 'Param Name Test Passed'},
                                   {   'code': '>>> layer = BatchNorm2d(7)\n>>> (list(torch.squeeze(layer.gamma).shape) == [7])  and (list(torch.squeeze(layer.beta).shape) == [7])\nTrue',
                                       'failure_message': 'Param Shape Test Failed',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0,
                                       'success_message': 'Param Shape Test Passed'}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
