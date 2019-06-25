# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  64: "SYMBOL_TYPE",
  65: "HEAP_NUMBER_TYPE",
  66: "BIGINT_TYPE",
  67: "ODDBALL_TYPE",
  68: "MAP_TYPE",
  69: "CODE_TYPE",
  70: "MUTABLE_HEAP_NUMBER_TYPE",
  71: "FOREIGN_TYPE",
  72: "BYTE_ARRAY_TYPE",
  73: "BYTECODE_ARRAY_TYPE",
  74: "FREE_SPACE_TYPE",
  75: "FIXED_DOUBLE_ARRAY_TYPE",
  76: "FEEDBACK_METADATA_TYPE",
  77: "FILLER_TYPE",
  78: "ACCESS_CHECK_INFO_TYPE",
  79: "ACCESSOR_INFO_TYPE",
  80: "ACCESSOR_PAIR_TYPE",
  81: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  82: "ALLOCATION_MEMENTO_TYPE",
  83: "ASM_WASM_DATA_TYPE",
  84: "ASYNC_GENERATOR_REQUEST_TYPE",
  85: "CLASS_POSITIONS_TYPE",
  86: "DEBUG_INFO_TYPE",
  87: "ENUM_CACHE_TYPE",
  88: "FUNCTION_TEMPLATE_INFO_TYPE",
  89: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  90: "INTERCEPTOR_INFO_TYPE",
  91: "INTERPRETER_DATA_TYPE",
  92: "OBJECT_TEMPLATE_INFO_TYPE",
  93: "PROMISE_CAPABILITY_TYPE",
  94: "PROMISE_REACTION_TYPE",
  95: "PROTOTYPE_INFO_TYPE",
  96: "SCRIPT_TYPE",
  97: "SOURCE_POSITION_TABLE_WITH_FRAME_CACHE_TYPE",
  98: "SOURCE_TEXT_MODULE_INFO_ENTRY_TYPE",
  99: "STACK_FRAME_INFO_TYPE",
  100: "STACK_TRACE_FRAME_TYPE",
  101: "TEMPLATE_OBJECT_DESCRIPTION_TYPE",
  102: "TUPLE2_TYPE",
  103: "TUPLE3_TYPE",
  104: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  105: "WASM_CAPI_FUNCTION_DATA_TYPE",
  106: "WASM_DEBUG_INFO_TYPE",
  107: "WASM_EXCEPTION_TAG_TYPE",
  108: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  109: "WASM_JS_FUNCTION_DATA_TYPE",
  110: "CALLABLE_TASK_TYPE",
  111: "CALLBACK_TASK_TYPE",
  112: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  113: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  114: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  115: "FINALIZATION_GROUP_CLEANUP_JOB_TASK_TYPE",
  116: "INTERNAL_CLASS_TYPE",
  117: "SMI_PAIR_TYPE",
  118: "SMI_BOX_TYPE",
  119: "SORT_STATE_TYPE",
  120: "ALLOCATION_SITE_TYPE",
  121: "EMBEDDER_DATA_ARRAY_TYPE",
  122: "FIXED_ARRAY_TYPE",
  123: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  124: "CLOSURE_FEEDBACK_CELL_ARRAY_TYPE",
  125: "HASH_TABLE_TYPE",
  126: "ORDERED_HASH_MAP_TYPE",
  127: "ORDERED_HASH_SET_TYPE",
  128: "ORDERED_NAME_DICTIONARY_TYPE",
  129: "NAME_DICTIONARY_TYPE",
  130: "GLOBAL_DICTIONARY_TYPE",
  131: "NUMBER_DICTIONARY_TYPE",
  132: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  133: "STRING_TABLE_TYPE",
  134: "EPHEMERON_HASH_TABLE_TYPE",
  135: "SCOPE_INFO_TYPE",
  136: "SCRIPT_CONTEXT_TABLE_TYPE",
  137: "AWAIT_CONTEXT_TYPE",
  138: "BLOCK_CONTEXT_TYPE",
  139: "CATCH_CONTEXT_TYPE",
  140: "DEBUG_EVALUATE_CONTEXT_TYPE",
  141: "EVAL_CONTEXT_TYPE",
  142: "FUNCTION_CONTEXT_TYPE",
  143: "MODULE_CONTEXT_TYPE",
  144: "NATIVE_CONTEXT_TYPE",
  145: "SCRIPT_CONTEXT_TYPE",
  146: "WITH_CONTEXT_TYPE",
  147: "WEAK_FIXED_ARRAY_TYPE",
  148: "TRANSITION_ARRAY_TYPE",
  149: "CALL_HANDLER_INFO_TYPE",
  150: "CELL_TYPE",
  151: "CODE_DATA_CONTAINER_TYPE",
  152: "DESCRIPTOR_ARRAY_TYPE",
  153: "FEEDBACK_CELL_TYPE",
  154: "FEEDBACK_VECTOR_TYPE",
  155: "LOAD_HANDLER_TYPE",
  156: "PREPARSE_DATA_TYPE",
  157: "PROPERTY_ARRAY_TYPE",
  158: "PROPERTY_CELL_TYPE",
  159: "SHARED_FUNCTION_INFO_TYPE",
  160: "SMALL_ORDERED_HASH_MAP_TYPE",
  161: "SMALL_ORDERED_HASH_SET_TYPE",
  162: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  163: "SOURCE_TEXT_MODULE_TYPE",
  164: "STORE_HANDLER_TYPE",
  165: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  166: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  167: "WEAK_ARRAY_LIST_TYPE",
  168: "WEAK_CELL_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_PRIMITIVE_WRAPPER_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  1064: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1065: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1066: "JS_DATE_TYPE",
  1067: "JS_ERROR_TYPE",
  1068: "JS_GENERATOR_OBJECT_TYPE",
  1069: "JS_MAP_TYPE",
  1070: "JS_MAP_KEY_ITERATOR_TYPE",
  1071: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1072: "JS_MAP_VALUE_ITERATOR_TYPE",
  1073: "JS_MESSAGE_OBJECT_TYPE",
  1074: "JS_PROMISE_TYPE",
  1075: "JS_REGEXP_TYPE",
  1076: "JS_REGEXP_STRING_ITERATOR_TYPE",
  1077: "JS_SET_TYPE",
  1078: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1079: "JS_SET_VALUE_ITERATOR_TYPE",
  1080: "JS_STRING_ITERATOR_TYPE",
  1081: "JS_WEAK_REF_TYPE",
  1082: "JS_FINALIZATION_GROUP_CLEANUP_ITERATOR_TYPE",
  1083: "JS_FINALIZATION_GROUP_TYPE",
  1084: "JS_WEAK_MAP_TYPE",
  1085: "JS_WEAK_SET_TYPE",
  1086: "JS_TYPED_ARRAY_TYPE",
  1087: "JS_DATA_VIEW_TYPE",
  1088: "JS_INTL_V8_BREAK_ITERATOR_TYPE",
  1089: "JS_INTL_COLLATOR_TYPE",
  1090: "JS_INTL_DATE_TIME_FORMAT_TYPE",
  1091: "JS_INTL_LIST_FORMAT_TYPE",
  1092: "JS_INTL_LOCALE_TYPE",
  1093: "JS_INTL_NUMBER_FORMAT_TYPE",
  1094: "JS_INTL_PLURAL_RULES_TYPE",
  1095: "JS_INTL_RELATIVE_TIME_FORMAT_TYPE",
  1096: "JS_INTL_SEGMENT_ITERATOR_TYPE",
  1097: "JS_INTL_SEGMENTER_TYPE",
  1098: "WASM_EXCEPTION_TYPE",
  1099: "WASM_GLOBAL_TYPE",
  1100: "WASM_INSTANCE_TYPE",
  1101: "WASM_MEMORY_TYPE",
  1102: "WASM_MODULE_TYPE",
  1103: "WASM_TABLE_TYPE",
  1104: "JS_BOUND_FUNCTION_TYPE",
  1105: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("read_only_space", 0x00139): (74, "FreeSpaceMap"),
  ("read_only_space", 0x00189): (68, "MetaMap"),
  ("read_only_space", 0x00209): (67, "NullMap"),
  ("read_only_space", 0x00271): (152, "DescriptorArrayMap"),
  ("read_only_space", 0x002d1): (147, "WeakFixedArrayMap"),
  ("read_only_space", 0x00321): (77, "OnePointerFillerMap"),
  ("read_only_space", 0x00371): (77, "TwoPointerFillerMap"),
  ("read_only_space", 0x003f1): (67, "UninitializedMap"),
  ("read_only_space", 0x00461): (8, "OneByteInternalizedStringMap"),
  ("read_only_space", 0x00501): (67, "UndefinedMap"),
  ("read_only_space", 0x00561): (65, "HeapNumberMap"),
  ("read_only_space", 0x005e1): (67, "TheHoleMap"),
  ("read_only_space", 0x00689): (67, "BooleanMap"),
  ("read_only_space", 0x00761): (72, "ByteArrayMap"),
  ("read_only_space", 0x007b1): (122, "FixedArrayMap"),
  ("read_only_space", 0x00801): (122, "FixedCOWArrayMap"),
  ("read_only_space", 0x00851): (125, "HashTableMap"),
  ("read_only_space", 0x008a1): (64, "SymbolMap"),
  ("read_only_space", 0x008f1): (40, "OneByteStringMap"),
  ("read_only_space", 0x00941): (135, "ScopeInfoMap"),
  ("read_only_space", 0x00991): (159, "SharedFunctionInfoMap"),
  ("read_only_space", 0x009e1): (69, "CodeMap"),
  ("read_only_space", 0x00a31): (142, "FunctionContextMap"),
  ("read_only_space", 0x00a81): (150, "CellMap"),
  ("read_only_space", 0x00ad1): (158, "GlobalPropertyCellMap"),
  ("read_only_space", 0x00b21): (71, "ForeignMap"),
  ("read_only_space", 0x00b71): (148, "TransitionArrayMap"),
  ("read_only_space", 0x00bc1): (154, "FeedbackVectorMap"),
  ("read_only_space", 0x00c61): (67, "ArgumentsMarkerMap"),
  ("read_only_space", 0x00d01): (67, "ExceptionMap"),
  ("read_only_space", 0x00da1): (67, "TerminationExceptionMap"),
  ("read_only_space", 0x00e49): (67, "OptimizedOutMap"),
  ("read_only_space", 0x00ee9): (67, "StaleRegisterMap"),
  ("read_only_space", 0x00f59): (144, "NativeContextMap"),
  ("read_only_space", 0x00fa9): (143, "ModuleContextMap"),
  ("read_only_space", 0x00ff9): (141, "EvalContextMap"),
  ("read_only_space", 0x01049): (145, "ScriptContextMap"),
  ("read_only_space", 0x01099): (137, "AwaitContextMap"),
  ("read_only_space", 0x010e9): (138, "BlockContextMap"),
  ("read_only_space", 0x01139): (139, "CatchContextMap"),
  ("read_only_space", 0x01189): (146, "WithContextMap"),
  ("read_only_space", 0x011d9): (140, "DebugEvaluateContextMap"),
  ("read_only_space", 0x01229): (136, "ScriptContextTableMap"),
  ("read_only_space", 0x01279): (124, "ClosureFeedbackCellArrayMap"),
  ("read_only_space", 0x012c9): (76, "FeedbackMetadataArrayMap"),
  ("read_only_space", 0x01319): (122, "ArrayListMap"),
  ("read_only_space", 0x01369): (66, "BigIntMap"),
  ("read_only_space", 0x013b9): (123, "ObjectBoilerplateDescriptionMap"),
  ("read_only_space", 0x01409): (73, "BytecodeArrayMap"),
  ("read_only_space", 0x01459): (151, "CodeDataContainerMap"),
  ("read_only_space", 0x014a9): (75, "FixedDoubleArrayMap"),
  ("read_only_space", 0x014f9): (130, "GlobalDictionaryMap"),
  ("read_only_space", 0x01549): (153, "ManyClosuresCellMap"),
  ("read_only_space", 0x01599): (122, "ModuleInfoMap"),
  ("read_only_space", 0x015e9): (70, "MutableHeapNumberMap"),
  ("read_only_space", 0x01639): (163, "SourceTextModuleMap"),
  ("read_only_space", 0x01689): (129, "NameDictionaryMap"),
  ("read_only_space", 0x016d9): (153, "NoClosuresCellMap"),
  ("read_only_space", 0x01729): (131, "NumberDictionaryMap"),
  ("read_only_space", 0x01779): (153, "OneClosureCellMap"),
  ("read_only_space", 0x017c9): (126, "OrderedHashMapMap"),
  ("read_only_space", 0x01819): (127, "OrderedHashSetMap"),
  ("read_only_space", 0x01869): (128, "OrderedNameDictionaryMap"),
  ("read_only_space", 0x018b9): (156, "PreparseDataMap"),
  ("read_only_space", 0x01909): (157, "PropertyArrayMap"),
  ("read_only_space", 0x01959): (149, "SideEffectCallHandlerInfoMap"),
  ("read_only_space", 0x019a9): (149, "SideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x019f9): (149, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x01a49): (132, "SimpleNumberDictionaryMap"),
  ("read_only_space", 0x01a99): (122, "SloppyArgumentsElementsMap"),
  ("read_only_space", 0x01ae9): (160, "SmallOrderedHashMapMap"),
  ("read_only_space", 0x01b39): (161, "SmallOrderedHashSetMap"),
  ("read_only_space", 0x01b89): (162, "SmallOrderedNameDictionaryMap"),
  ("read_only_space", 0x01bd9): (133, "StringTableMap"),
  ("read_only_space", 0x01c29): (165, "UncompiledDataWithoutPreparseDataMap"),
  ("read_only_space", 0x01c79): (166, "UncompiledDataWithPreparseDataMap"),
  ("read_only_space", 0x01cc9): (167, "WeakArrayListMap"),
  ("read_only_space", 0x01d19): (134, "EphemeronHashTableMap"),
  ("read_only_space", 0x01d69): (121, "EmbedderDataArrayMap"),
  ("read_only_space", 0x01db9): (168, "WeakCellMap"),
  ("read_only_space", 0x01e09): (58, "NativeSourceStringMap"),
  ("read_only_space", 0x01e59): (32, "StringMap"),
  ("read_only_space", 0x01ea9): (41, "ConsOneByteStringMap"),
  ("read_only_space", 0x01ef9): (33, "ConsStringMap"),
  ("read_only_space", 0x01f49): (45, "ThinOneByteStringMap"),
  ("read_only_space", 0x01f99): (37, "ThinStringMap"),
  ("read_only_space", 0x01fe9): (35, "SlicedStringMap"),
  ("read_only_space", 0x02039): (43, "SlicedOneByteStringMap"),
  ("read_only_space", 0x02089): (34, "ExternalStringMap"),
  ("read_only_space", 0x020d9): (42, "ExternalOneByteStringMap"),
  ("read_only_space", 0x02129): (50, "UncachedExternalStringMap"),
  ("read_only_space", 0x02179): (0, "InternalizedStringMap"),
  ("read_only_space", 0x021c9): (2, "ExternalInternalizedStringMap"),
  ("read_only_space", 0x02219): (10, "ExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x02269): (18, "UncachedExternalInternalizedStringMap"),
  ("read_only_space", 0x022b9): (26, "UncachedExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x02309): (58, "UncachedExternalOneByteStringMap"),
  ("read_only_space", 0x02359): (67, "SelfReferenceMarkerMap"),
  ("read_only_space", 0x023c1): (87, "EnumCacheMap"),
  ("read_only_space", 0x02461): (104, "ArrayBoilerplateDescriptionMap"),
  ("read_only_space", 0x02651): (90, "InterceptorInfoMap"),
  ("read_only_space", 0x04e31): (78, "AccessCheckInfoMap"),
  ("read_only_space", 0x04e81): (79, "AccessorInfoMap"),
  ("read_only_space", 0x04ed1): (80, "AccessorPairMap"),
  ("read_only_space", 0x04f21): (81, "AliasedArgumentsEntryMap"),
  ("read_only_space", 0x04f71): (82, "AllocationMementoMap"),
  ("read_only_space", 0x04fc1): (83, "AsmWasmDataMap"),
  ("read_only_space", 0x05011): (84, "AsyncGeneratorRequestMap"),
  ("read_only_space", 0x05061): (85, "ClassPositionsMap"),
  ("read_only_space", 0x050b1): (86, "DebugInfoMap"),
  ("read_only_space", 0x05101): (88, "FunctionTemplateInfoMap"),
  ("read_only_space", 0x05151): (89, "FunctionTemplateRareDataMap"),
  ("read_only_space", 0x051a1): (91, "InterpreterDataMap"),
  ("read_only_space", 0x051f1): (92, "ObjectTemplateInfoMap"),
  ("read_only_space", 0x05241): (93, "PromiseCapabilityMap"),
  ("read_only_space", 0x05291): (94, "PromiseReactionMap"),
  ("read_only_space", 0x052e1): (95, "PrototypeInfoMap"),
  ("read_only_space", 0x05331): (96, "ScriptMap"),
  ("read_only_space", 0x05381): (97, "SourcePositionTableWithFrameCacheMap"),
  ("read_only_space", 0x053d1): (98, "SourceTextModuleInfoEntryMap"),
  ("read_only_space", 0x05421): (99, "StackFrameInfoMap"),
  ("read_only_space", 0x05471): (100, "StackTraceFrameMap"),
  ("read_only_space", 0x054c1): (101, "TemplateObjectDescriptionMap"),
  ("read_only_space", 0x05511): (102, "Tuple2Map"),
  ("read_only_space", 0x05561): (103, "Tuple3Map"),
  ("read_only_space", 0x055b1): (105, "WasmCapiFunctionDataMap"),
  ("read_only_space", 0x05601): (106, "WasmDebugInfoMap"),
  ("read_only_space", 0x05651): (107, "WasmExceptionTagMap"),
  ("read_only_space", 0x056a1): (108, "WasmExportedFunctionDataMap"),
  ("read_only_space", 0x056f1): (109, "WasmJSFunctionDataMap"),
  ("read_only_space", 0x05741): (110, "CallableTaskMap"),
  ("read_only_space", 0x05791): (111, "CallbackTaskMap"),
  ("read_only_space", 0x057e1): (112, "PromiseFulfillReactionJobTaskMap"),
  ("read_only_space", 0x05831): (113, "PromiseRejectReactionJobTaskMap"),
  ("read_only_space", 0x05881): (114, "PromiseResolveThenableJobTaskMap"),
  ("read_only_space", 0x058d1): (115, "FinalizationGroupCleanupJobTaskMap"),
  ("read_only_space", 0x05921): (116, "InternalClassMap"),
  ("read_only_space", 0x05971): (117, "SmiPairMap"),
  ("read_only_space", 0x059c1): (118, "SmiBoxMap"),
  ("read_only_space", 0x05a11): (119, "SortStateMap"),
  ("read_only_space", 0x05a61): (120, "AllocationSiteWithWeakNextMap"),
  ("read_only_space", 0x05ab1): (120, "AllocationSiteWithoutWeakNextMap"),
  ("read_only_space", 0x05b01): (155, "LoadHandler1Map"),
  ("read_only_space", 0x05b51): (155, "LoadHandler2Map"),
  ("read_only_space", 0x05ba1): (155, "LoadHandler3Map"),
  ("read_only_space", 0x05bf1): (164, "StoreHandler0Map"),
  ("read_only_space", 0x05c41): (164, "StoreHandler1Map"),
  ("read_only_space", 0x05c91): (164, "StoreHandler2Map"),
  ("read_only_space", 0x05ce1): (164, "StoreHandler3Map"),
  ("map_space", 0x00139): (1057, "ExternalMap"),
  ("map_space", 0x00189): (1073, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("read_only_space", 0x001d9): "NullValue",
  ("read_only_space", 0x00259): "EmptyDescriptorArray",
  ("read_only_space", 0x002c1): "EmptyWeakFixedArray",
  ("read_only_space", 0x003c1): "UninitializedValue",
  ("read_only_space", 0x004d1): "UndefinedValue",
  ("read_only_space", 0x00551): "NanValue",
  ("read_only_space", 0x005b1): "TheHoleValue",
  ("read_only_space", 0x00649): "HoleNanValue",
  ("read_only_space", 0x00659): "TrueValue",
  ("read_only_space", 0x00709): "FalseValue",
  ("read_only_space", 0x00751): "empty_string",
  ("read_only_space", 0x00c11): "EmptyScopeInfo",
  ("read_only_space", 0x00c21): "EmptyFixedArray",
  ("read_only_space", 0x00c31): "ArgumentsMarker",
  ("read_only_space", 0x00cd1): "Exception",
  ("read_only_space", 0x00d71): "TerminationException",
  ("read_only_space", 0x00e19): "OptimizedOut",
  ("read_only_space", 0x00eb9): "StaleRegister",
  ("read_only_space", 0x023a9): "EmptyEnumCache",
  ("read_only_space", 0x02411): "EmptyPropertyArray",
  ("read_only_space", 0x02421): "EmptyByteArray",
  ("read_only_space", 0x02431): "EmptyObjectBoilerplateDescription",
  ("read_only_space", 0x02449): "EmptyArrayBoilerplateDescription",
  ("read_only_space", 0x024b1): "EmptyClosureFeedbackCellArray",
  ("read_only_space", 0x024c1): "EmptySloppyArgumentsElements",
  ("read_only_space", 0x024e1): "EmptySlowElementDictionary",
  ("read_only_space", 0x02529): "EmptyOrderedHashMap",
  ("read_only_space", 0x02551): "EmptyOrderedHashSet",
  ("read_only_space", 0x02579): "EmptyFeedbackMetadata",
  ("read_only_space", 0x02589): "EmptyPropertyCell",
  ("read_only_space", 0x025b1): "EmptyPropertyDictionary",
  ("read_only_space", 0x02601): "NoOpInterceptorInfo",
  ("read_only_space", 0x026a1): "EmptyWeakArrayList",
  ("read_only_space", 0x026b9): "InfinityValue",
  ("read_only_space", 0x026c9): "MinusZeroValue",
  ("read_only_space", 0x026d9): "MinusInfinityValue",
  ("read_only_space", 0x026e9): "SelfReferenceMarker",
  ("read_only_space", 0x02741): "OffHeapTrampolineRelocationInfo",
  ("read_only_space", 0x02759): "TrampolineTrivialCodeDataContainer",
  ("read_only_space", 0x02771): "TrampolinePromiseRejectionCodeDataContainer",
  ("read_only_space", 0x02789): "HashSeed",
  ("old_space", 0x00139): "ArgumentsIteratorAccessor",
  ("old_space", 0x001a9): "ArrayLengthAccessor",
  ("old_space", 0x00219): "BoundFunctionLengthAccessor",
  ("old_space", 0x00289): "BoundFunctionNameAccessor",
  ("old_space", 0x002f9): "ErrorStackAccessor",
  ("old_space", 0x00369): "FunctionArgumentsAccessor",
  ("old_space", 0x003d9): "FunctionCallerAccessor",
  ("old_space", 0x00449): "FunctionNameAccessor",
  ("old_space", 0x004b9): "FunctionLengthAccessor",
  ("old_space", 0x00529): "FunctionPrototypeAccessor",
  ("old_space", 0x00599): "StringLengthAccessor",
  ("old_space", 0x00609): "InvalidPrototypeValidityCell",
  ("old_space", 0x00619): "EmptyScript",
  ("old_space", 0x00699): "ManyClosuresCell",
  ("old_space", 0x006b1): "ArrayConstructorProtector",
  ("old_space", 0x006c1): "NoElementsProtector",
  ("old_space", 0x006e9): "IsConcatSpreadableProtector",
  ("old_space", 0x006f9): "ArraySpeciesProtector",
  ("old_space", 0x00721): "TypedArraySpeciesProtector",
  ("old_space", 0x00749): "RegExpSpeciesProtector",
  ("old_space", 0x00771): "PromiseSpeciesProtector",
  ("old_space", 0x00799): "StringLengthProtector",
  ("old_space", 0x007a9): "ArrayIteratorProtector",
  ("old_space", 0x007d1): "ArrayBufferDetachingProtector",
  ("old_space", 0x007f9): "PromiseHookProtector",
  ("old_space", 0x00821): "PromiseResolveProtector",
  ("old_space", 0x00831): "MapIteratorProtector",
  ("old_space", 0x00859): "PromiseThenProtector",
  ("old_space", 0x00881): "SetIteratorProtector",
  ("old_space", 0x008a9): "StringIteratorProtector",
  ("old_space", 0x008d1): "SingleCharacterStringCache",
  ("old_space", 0x010e1): "StringSplitCache",
  ("old_space", 0x018f1): "RegExpMultipleCache",
  ("old_space", 0x02101): "BuiltinsConstantsTable",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "WASM_EXIT",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
