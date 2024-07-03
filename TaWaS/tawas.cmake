# Self-describing NUOPC Component for ESMX

add_library(tawas STATIC IMPORTED)
set_target_properties(tawas PROPERTIES
  IMPORTED_LOCATION             /home/dev/ESMX_AtmOcnProto/TaWaS/libtawas.a
  INTERFACE_INCLUDE_DIRECTORIES /home/dev/ESMX_AtmOcnProto/TaWaS
#  INTERFACE_LINK_DIRECTORIES    <not-needed-here>
#  INTERFACE_LINK_LIBRARIES      <not-needed-here>
)
target_link_libraries(esmx_driver PUBLIC tawas)
