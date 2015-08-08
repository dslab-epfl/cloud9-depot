#
# Cloud9 Parallel Symbolic Execution Engine
# 

{
  'targets': [
    {
      'target_name': 'AllTestingTargets',
      'type': 'none',
      'dependencies': [
        'libcxx.gyp:*',
        '../examples/examples.gyp:*',
      ],
    },
  ],
}
