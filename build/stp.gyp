#
# Cloud9 Parallel Symbolic Execution Engine
#

{
  'variables': {
    'stp_path': '../third_party/stp',
    'stp_src': '../third_party/stp/src',
    'valid_extensions': [
      '-name', '*.h',
      '-o', '-name', '*.hpp',
      '-o', '-name', '*.cpp',
      '-o', '-name', '*.c',
    ],
    'lex_tool': 'flex',
    'yacc_tool': 'bison -d -y --debug -v',
  }, # variables
  
  'target_defaults': {
    'cflags': [
      '-O3',
      '-fomit-frame-pointer',
      '-Wno-deprecated',
    ],
    'defines': [
      'NDEBUG',
      # Required by MiniSAT
      '__STDC_LIMIT_MACROS',
      '__STDC_FORMAT_MACROS',
      'EXT_HASH_MAP',
    ],
  }, # target_defaults
  
  'targets': [
    {
      'target_name': 'libast',
      'type': 'static_library',
      'sources': [
        '<!@(find <(stp_src)/AST -maxdepth 1 <(valid_extensions))',
        '<!@(find <(stp_src)/AST/NodeFactory -maxdepth 1 <(valid_extensions))',
        '<!@(find <(stp_src)/c_interface -maxdepth 1 <(valid_extensions))',
        '<!@(find <(stp_src)/cpp_interface -maxdepth 1 <(valid_extensions))',
        '<!@(find <(stp_src)/to-sat <(valid_extensions))',
      ],
    },
    {
      'target_name': 'libstpmgr',
      'type': 'static_library',
      'sources': [
        '<!@(find <(stp_src)/STPManager -maxdepth 1 <(valid_extensions))',
      ],
    },
    {
      'target_name': 'libprinter',
      'type': 'static_library',
      'sources': [
        '<!@(find <(stp_src)/printer -maxdepth 1 <(valid_extensions))',
      ],
    },
    {
      'target_name': 'libabstractionrefinement',
      'type': 'static_library',
      'sources': [
        '<!@(find <(stp_src)/absrefine_counterexample -maxdepth 1 <@(valid_extensions))',   
      ],
    },
  ], # targets
}
