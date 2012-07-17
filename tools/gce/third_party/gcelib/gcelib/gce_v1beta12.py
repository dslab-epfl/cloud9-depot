# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Generated code for the Compute Engine API.

This generated code is for version v1beta12 of the API.

Documentation can be found at:
  https://developers.google.com/compute/docs/reference/v1beta12
"""

import gce_base
import json


class AccessConfig(object):
  """Generated class AccessConfig."""
  __slots__ = ['name', 'natIP', 'type']

  def __init__(self, name=None, natIP=None, type=None):
    self.name = name
    self.natIP = natIP
    self.type = type

  def __str__(self):
    return '<AccessConfig instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(AccessConfig.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#accessConfig':
      raise ValueError('Cannot load AccessConfig from {0}.'.format(kind))

    return AccessConfig(
        resource.get('name'),
        resource.get('natIP'),
        resource.get('type'))

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#accessConfig'}
    if isinstance(value, AccessConfig):
      if value.name is not None:
        result['name'] = value.name
      if value.natIP is not None:
        result['natIP'] = value.natIP
      if value.type is not None:
        result['type'] = value.type
    elif isinstance(value, dict):
      temp = value.get('name')
      if temp is not None:
        result['name'] = temp
      temp = value.get('natIP')
      if temp is not None:
        result['natIP'] = temp
      temp = value.get('type')
      if temp is not None:
        result['type'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [AccessConfig.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value):
    if value is None:
      return []
    elif isinstance(value, list):
      return [AccessConfig.to_json(item) for item in value]
    elif isinstance(value, dict) or isinstance(value, AccessConfig):
      return [AccessConfig.to_json(value)]


class AttachedDisk(object):
  """Generated class AttachedDisk."""
  __slots__ = ['type', 'deleteOnTerminate', 'deviceName', 'index', 'mode', 'source']

  def __init__(self, type=None, deleteOnTerminate=None, deviceName=None, index=None, mode=None, source=None):
    self.type = type
    self.deleteOnTerminate = deleteOnTerminate
    self.deviceName = deviceName
    self.index = index
    self.mode = mode
    self.source = source

  def __str__(self):
    return '<AttachedDisk instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(AttachedDisk.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#attachedDisk':
      raise ValueError('Cannot load AttachedDisk from {0}.'.format(kind))

    return AttachedDisk(
        resource.get('type'),
        resource.get('deleteOnTerminate'),
        resource.get('deviceName'),
        resource.get('index'),
        resource.get('mode'),
        resource.get('source'))

  @staticmethod
  def to_json(value, gce=None, project=None):
    result = {'kind': 'compute#attachedDisk'}
    if isinstance(value, AttachedDisk):
      if value.type is not None:
        result['type'] = value.type
      if value.deleteOnTerminate is not None:
        result['deleteOnTerminate'] = value.deleteOnTerminate
      if value.deviceName is not None:
        result['deviceName'] = value.deviceName
      if value.index is not None:
        result['index'] = value.index
      if value.mode is not None:
        result['mode'] = value.mode
      if value.source is not None:
        result['source'] = (gce._normalize(project, 'disks', value.source) if (gce is not None and project is not None) else value.source)
    elif isinstance(value, dict):
      temp = value.get('type')
      if temp is not None:
        result['type'] = temp
      temp = value.get('deleteOnTerminate')
      if temp is not None:
        result['deleteOnTerminate'] = temp
      temp = value.get('deviceName')
      if temp is not None:
        result['deviceName'] = temp
      temp = value.get('index')
      if temp is not None:
        result['index'] = temp
      temp = value.get('mode')
      if temp is not None:
        result['mode'] = temp
      temp = value.get('source')
      if temp is not None:
        result['source'] = (gce._normalize(project, 'disks', temp) if (gce is not None and project is not None) else temp)
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [AttachedDisk.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value, gce, project):
    if value is None:
      return []
    elif isinstance(value, list):
      return [AttachedDisk.to_json(item, gce, project) for item in value]
    elif isinstance(value, dict) or isinstance(value, AttachedDisk):
      return [AttachedDisk.to_json(value, gce, project)]


class Disk(object):
  """Generated class Disk."""
  __slots__ = ['sizeGb', 'zone', 'description', 'name', 'sourceSnapshot', 'sourceSnapshotId', 'options', 'status', 'creationTimestamp', 'id', 'selfLink', '__gce', '__project']

  def __init__(self, sizeGb=None, zone=None, description=None, name=None, sourceSnapshot=None, sourceSnapshotId=None, options=None, status=None):
    self.__gce = None
    self.__project = None
    self.sizeGb = sizeGb
    self.zone = zone
    self.description = description
    self.name = name
    self.sourceSnapshot = sourceSnapshot
    self.sourceSnapshotId = sourceSnapshotId
    self.options = options
    self.status = status
    self.creationTimestamp = None
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<Disk instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(Disk.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#disk':
      raise ValueError('Cannot load Disk from {0}.'.format(kind))

    result = Disk(
        resource.get('sizeGb'),
        resource.get('zone'),
        resource.get('description'),
        resource.get('name'),
        resource.get('sourceSnapshot'),
        resource.get('sourceSnapshotId'),
        resource.get('options'),
        resource.get('status'))

    result.creationTimestamp = resource.get('creationTimestamp')
    result.id = resource.get('id')
    self_link = resource.get('selfLink')
    result.selfLink = self_link
    result.__gce = gce
    result.__project = gce_base.GoogleComputeEngineBase._parse_project(self_link)
    return result

  @staticmethod
  def to_json(value, gce=None, project=None):
    result = {'kind': 'compute#disk'}
    if isinstance(value, Disk):
      if value.sizeGb is not None:
        result['sizeGb'] = value.sizeGb
      if value.zone is not None:
        result['zone'] = (gce._normalize(project, 'zones', value.zone) if (gce is not None and project is not None) else value.zone)
      if value.description is not None:
        result['description'] = value.description
      if value.name is not None:
        result['name'] = value.name
      if value.sourceSnapshot is not None:
        result['sourceSnapshot'] = value.sourceSnapshot
      if value.sourceSnapshotId is not None:
        result['sourceSnapshotId'] = value.sourceSnapshotId
      if value.options is not None:
        result['options'] = value.options
      if value.status is not None:
        result['status'] = value.status
      if value.creationTimestamp is not None:
        result['creationTimestamp'] = value.creationTimestamp
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('sizeGb')
      if temp is not None:
        result['sizeGb'] = temp
      temp = value.get('zone')
      if temp is not None:
        result['zone'] = (gce._normalize(project, 'zones', temp) if (gce is not None and project is not None) else temp)
      temp = value.get('description')
      if temp is not None:
        result['description'] = temp
      temp = value.get('name')
      if temp is not None:
        result['name'] = temp
      temp = value.get('sourceSnapshot')
      if temp is not None:
        result['sourceSnapshot'] = temp
      temp = value.get('sourceSnapshotId')
      if temp is not None:
        result['sourceSnapshotId'] = temp
      temp = value.get('options')
      if temp is not None:
        result['options'] = temp
      temp = value.get('status')
      if temp is not None:
        result['status'] = temp
      temp = value.get('creationTimestamp')
      if temp is not None:
        result['creationTimestamp'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [Disk.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value, gce, project):
    if value is None:
      return []
    elif isinstance(value, list):
      return [Disk.to_json(item, gce, project) for item in value]
    elif isinstance(value, dict) or isinstance(value, Disk):
      return [Disk.to_json(value, gce, project)]

  def insert(self, sizeGb=None, zone=None, description=None, name=None, project=None, sourceSnapshot=None, sourceSnapshotId=None, options=None, status=None, blocking=True, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.insert_disk(self, sizeGb, zone, description, name, project, sourceSnapshot, sourceSnapshotId, options, status, blocking)

  def get(self, project=None, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.get_disk(self, project)

  def delete(self, project=None, blocking=True, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.delete_disk(self, project, blocking)


class DiskList(gce_base.ListObjectBase):
  """Generated class DiskList."""
  __slots__ = ['items', 'nextPageToken', 'id', 'selfLink']

  def __init__(self, items=None, nextPageToken=None):
    gce_base.ListObjectBase.__init__(self, items)
    self.items = items
    self.nextPageToken = nextPageToken
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<DiskList instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(DiskList.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#diskList':
      raise ValueError('Cannot load DiskList from {0}.'.format(kind))

    result = DiskList(
        Disk.array_from_json(resource.get('items'), gce),
        resource.get('nextPageToken'))

    result.id = resource.get('id')
    result.selfLink = resource.get('selfLink')
    return result

  @staticmethod
  def to_json(value, gce=None, project=None):
    result = {'kind': 'compute#diskList'}
    if isinstance(value, DiskList):
      if value.items is not None:
        result['items'] = Disk.array_to_json(value.items, gce, project)
      if value.nextPageToken is not None:
        result['nextPageToken'] = value.nextPageToken
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('items')
      if temp is not None:
        result['items'] = Disk.array_to_json(temp, gce, project)
      temp = value.get('nextPageToken')
      if temp is not None:
        result['nextPageToken'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result


class Firewall(object):
  """Generated class Firewall."""
  __slots__ = ['network', 'allowed', 'sourceRanges', 'sourceTags', 'targetTags', 'description', 'name', 'creationTimestamp', 'id', 'selfLink', '__gce', '__project']

  def __init__(self, network=None, allowed=None, sourceRanges=None, sourceTags=None, targetTags=None, description=None, name=None):
    self.__gce = None
    self.__project = None
    self.network = network
    self.allowed = allowed
    self.sourceRanges = sourceRanges
    self.sourceTags = sourceTags
    self.targetTags = targetTags
    self.description = description
    self.name = name
    self.creationTimestamp = None
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<Firewall instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(Firewall.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#firewall':
      raise ValueError('Cannot load Firewall from {0}.'.format(kind))

    result = Firewall(
        resource.get('network'),
        _Allowed.array_from_json(resource.get('allowed'), gce),
        gce_base.GoogleComputeEngineBase._json_to_strings(resource.get('sourceRanges')),
        gce_base.GoogleComputeEngineBase._json_to_strings(resource.get('sourceTags')),
        gce_base.GoogleComputeEngineBase._json_to_strings(resource.get('targetTags')),
        resource.get('description'),
        resource.get('name'))

    result.creationTimestamp = resource.get('creationTimestamp')
    result.id = resource.get('id')
    self_link = resource.get('selfLink')
    result.selfLink = self_link
    result.__gce = gce
    result.__project = gce_base.GoogleComputeEngineBase._parse_project(self_link)
    return result

  @staticmethod
  def to_json(value, gce=None, project=None):
    result = {'kind': 'compute#firewall'}
    if isinstance(value, Firewall):
      if value.network is not None:
        result['network'] = (gce._normalize(project, 'networks', value.network) if (gce is not None and project is not None) else value.network)
      if value.allowed is not None:
        result['allowed'] = _Allowed.array_to_json(value.allowed)
      if value.sourceRanges is not None:
        result['sourceRanges'] = gce_base.GoogleComputeEngineBase._strings_to_json(value.sourceRanges)
      if value.sourceTags is not None:
        result['sourceTags'] = gce_base.GoogleComputeEngineBase._strings_to_json(value.sourceTags)
      if value.targetTags is not None:
        result['targetTags'] = gce_base.GoogleComputeEngineBase._strings_to_json(value.targetTags)
      if value.description is not None:
        result['description'] = value.description
      if value.name is not None:
        result['name'] = value.name
      if value.creationTimestamp is not None:
        result['creationTimestamp'] = value.creationTimestamp
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('network')
      if temp is not None:
        result['network'] = (gce._normalize(project, 'networks', temp) if (gce is not None and project is not None) else temp)
      temp = value.get('allowed')
      if temp is not None:
        result['allowed'] = _Allowed.array_to_json(temp)
      temp = value.get('sourceRanges')
      if temp is not None:
        result['sourceRanges'] = gce_base.GoogleComputeEngineBase._strings_to_json(temp)
      temp = value.get('sourceTags')
      if temp is not None:
        result['sourceTags'] = gce_base.GoogleComputeEngineBase._strings_to_json(temp)
      temp = value.get('targetTags')
      if temp is not None:
        result['targetTags'] = gce_base.GoogleComputeEngineBase._strings_to_json(temp)
      temp = value.get('description')
      if temp is not None:
        result['description'] = temp
      temp = value.get('name')
      if temp is not None:
        result['name'] = temp
      temp = value.get('creationTimestamp')
      if temp is not None:
        result['creationTimestamp'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [Firewall.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value, gce, project):
    if value is None:
      return []
    elif isinstance(value, list):
      return [Firewall.to_json(item, gce, project) for item in value]
    elif isinstance(value, dict) or isinstance(value, Firewall):
      return [Firewall.to_json(value, gce, project)]

  def insert(self, network=None, allowed=None, sourceRanges=None, sourceTags=None, targetTags=None, description=None, name=None, project=None, blocking=True, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.insert_firewall(self, network, allowed, sourceRanges, sourceTags, targetTags, description, name, project, blocking)

  def get(self, project=None, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.get_firewall(self, project)

  def update(self, network=None, allowed=None, sourceRanges=None, sourceTags=None, targetTags=None, description=None, name=None, project=None, blocking=True, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.update_firewall(self, network, allowed, sourceRanges, sourceTags, targetTags, description, name, project, blocking)

  def patch(self, network=None, allowed=None, sourceRanges=None, sourceTags=None, targetTags=None, description=None, name=None, project=None, blocking=True, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.patch_firewall(self, network, allowed, sourceRanges, sourceTags, targetTags, description, name, project, blocking)

  def delete(self, project=None, blocking=True, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.delete_firewall(self, project, blocking)


class FirewallList(gce_base.ListObjectBase):
  """Generated class FirewallList."""
  __slots__ = ['id', 'items', 'nextPageToken', 'selfLink']

  def __init__(self, id=None, items=None, nextPageToken=None):
    gce_base.ListObjectBase.__init__(self, items)
    self.id = id
    self.items = items
    self.nextPageToken = nextPageToken
    self.selfLink = None

  def __str__(self):
    return '<FirewallList instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(FirewallList.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#firewallList':
      raise ValueError('Cannot load FirewallList from {0}.'.format(kind))

    result = FirewallList(
        resource.get('id'),
        Firewall.array_from_json(resource.get('items'), gce),
        resource.get('nextPageToken'))

    result.selfLink = resource.get('selfLink')
    return result

  @staticmethod
  def to_json(value, gce=None, project=None):
    result = {'kind': 'compute#firewallList'}
    if isinstance(value, FirewallList):
      if value.id is not None:
        result['id'] = value.id
      if value.items is not None:
        result['items'] = Firewall.array_to_json(value.items, gce, project)
      if value.nextPageToken is not None:
        result['nextPageToken'] = value.nextPageToken
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('items')
      if temp is not None:
        result['items'] = Firewall.array_to_json(temp, gce, project)
      temp = value.get('nextPageToken')
      if temp is not None:
        result['nextPageToken'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result


class Image(object):
  """Generated class Image."""
  __slots__ = ['sourceType', 'rawDiskSource', 'rawDiskContainerType', 'description', 'name', 'rawDiskSha1Checksum', 'diskSnapshotSource', 'preferredKernel', 'creationTimestamp', 'id', 'selfLink', '__gce', '__project']

  def __init__(self, sourceType=None, rawDiskSource=None, rawDiskContainerType=None, description=None, name=None, rawDiskSha1Checksum=None, diskSnapshotSource=None, preferredKernel=None):
    self.__gce = None
    self.__project = None
    self.sourceType = sourceType
    self.rawDiskSource = rawDiskSource
    self.rawDiskContainerType = rawDiskContainerType
    self.description = description
    self.name = name
    self.rawDiskSha1Checksum = rawDiskSha1Checksum
    self.diskSnapshotSource = diskSnapshotSource
    self.preferredKernel = preferredKernel
    self.creationTimestamp = None
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<Image instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(Image.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#image':
      raise ValueError('Cannot load Image from {0}.'.format(kind))

    rawDiskSource = None
    rawDiskContainerType = None
    rawDiskSha1Checksum = None
    diskSnapshotSource = None
    __temp = resource.get('rawDisk')
    if __temp is not None:
      rawDiskContainerType = __temp.get('containerType')
      rawDiskSource = __temp.get('source')
      rawDiskSha1Checksum = __temp.get('sha1Checksum')
    __temp = resource.get('diskSnapshot')
    if __temp is not None:
      diskSnapshotSource = __temp.get('source')
    result = Image(
        resource.get('sourceType'),
        rawDiskSource,
        rawDiskContainerType,
        resource.get('description'),
        resource.get('name'),
        rawDiskSha1Checksum,
        diskSnapshotSource,
        resource.get('preferredKernel'))

    result.creationTimestamp = resource.get('creationTimestamp')
    result.id = resource.get('id')
    self_link = resource.get('selfLink')
    result.selfLink = self_link
    result.__gce = gce
    result.__project = gce_base.GoogleComputeEngineBase._parse_project(self_link)
    return result

  @staticmethod
  def to_json(value, gce=None, project=None):
    result = {'kind': 'compute#image'}
    if isinstance(value, Image):
      if value.sourceType is not None:
        result['sourceType'] = value.sourceType
      if value.rawDiskContainerType is not None or value.rawDiskSource is not None or value.rawDiskSha1Checksum is not None:
        __temp = {}
        if value.rawDiskContainerType is not None:
          __temp['containerType'] = value.rawDiskContainerType
        if value.rawDiskSource is not None:
          __temp['source'] = value.rawDiskSource
        if value.rawDiskSha1Checksum is not None:
          __temp['sha1Checksum'] = value.rawDiskSha1Checksum
        result['rawDisk'] = __temp
      if value.description is not None:
        result['description'] = value.description
      if value.name is not None:
        result['name'] = value.name
      if value.diskSnapshotSource is not None:
        __temp = {}
        if value.diskSnapshotSource is not None:
          __temp['source'] = (gce._normalize(project, 'disks', value.diskSnapshotSource) if (gce is not None and project is not None) else value.diskSnapshotSource)
        result['diskSnapshot'] = __temp
      if value.preferredKernel is not None:
        result['preferredKernel'] = (gce._normalize(project, 'kernels', value.preferredKernel) if (gce is not None and project is not None) else value.preferredKernel)
      if value.creationTimestamp is not None:
        result['creationTimestamp'] = value.creationTimestamp
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('sourceType')
      if temp is not None:
        result['sourceType'] = temp
      __temp = value.get('rawDisk')
      if __temp is not None:
        __temp_1 = {}
        temp = __temp.get('containerType')
        if temp is not None:
          __temp_1['containerType'] = temp
        temp = __temp.get('source')
        if temp is not None:
          __temp_1['source'] = temp
        temp = __temp.get('sha1Checksum')
        if temp is not None:
          __temp_1['sha1Checksum'] = temp
        result['rawDisk'] = __temp_1
      temp = value.get('description')
      if temp is not None:
        result['description'] = temp
      temp = value.get('name')
      if temp is not None:
        result['name'] = temp
      __temp = value.get('diskSnapshot')
      if __temp is not None:
        __temp_1 = {}
        temp = __temp.get('source')
        if temp is not None:
          __temp_1['source'] = (gce._normalize(project, 'disks', temp) if (gce is not None and project is not None) else temp)
        result['diskSnapshot'] = __temp_1
      temp = value.get('preferredKernel')
      if temp is not None:
        result['preferredKernel'] = (gce._normalize(project, 'kernels', temp) if (gce is not None and project is not None) else temp)
      temp = value.get('creationTimestamp')
      if temp is not None:
        result['creationTimestamp'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [Image.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value, gce, project):
    if value is None:
      return []
    elif isinstance(value, list):
      return [Image.to_json(item, gce, project) for item in value]
    elif isinstance(value, dict) or isinstance(value, Image):
      return [Image.to_json(value, gce, project)]

  def insert(self, sourceType=None, rawDiskSource=None, rawDiskContainerType=None, description=None, name=None, rawDiskSha1Checksum=None, diskSnapshotSource=None, preferredKernel=None, project=None, blocking=True, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.insert_image(self, sourceType, rawDiskSource, rawDiskContainerType, description, name, rawDiskSha1Checksum, diskSnapshotSource, preferredKernel, project, blocking)

  def get(self, project=None, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.get_image(self, project)

  def delete(self, project=None, blocking=True, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.delete_image(self, project, blocking)


class ImageList(gce_base.ListObjectBase):
  """Generated class ImageList."""
  __slots__ = ['items', 'nextPageToken', 'id', 'selfLink']

  def __init__(self, items=None, nextPageToken=None):
    gce_base.ListObjectBase.__init__(self, items)
    self.items = items
    self.nextPageToken = nextPageToken
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<ImageList instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(ImageList.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#imageList':
      raise ValueError('Cannot load ImageList from {0}.'.format(kind))

    result = ImageList(
        Image.array_from_json(resource.get('items'), gce),
        resource.get('nextPageToken'))

    result.id = resource.get('id')
    result.selfLink = resource.get('selfLink')
    return result

  @staticmethod
  def to_json(value, gce=None, project=None):
    result = {'kind': 'compute#imageList'}
    if isinstance(value, ImageList):
      if value.items is not None:
        result['items'] = Image.array_to_json(value.items, gce, project)
      if value.nextPageToken is not None:
        result['nextPageToken'] = value.nextPageToken
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('items')
      if temp is not None:
        result['items'] = Image.array_to_json(temp, gce, project)
      temp = value.get('nextPageToken')
      if temp is not None:
        result['nextPageToken'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result


class Instance(object):
  """Generated class Instance."""
  __slots__ = ['networkInterfaces', 'metadata', 'disks', 'machineType', 'serviceAccounts', 'tags', 'image', 'zone', 'description', 'name', 'creationTimestamp', 'id', 'selfLink', 'status', 'statusMessage', '__gce', '__project']

  def __init__(self, networkInterfaces=None, metadata=None, disks=None, machineType=None, serviceAccounts=None, tags=None, image=None, zone=None, description=None, name=None):
    self.__gce = None
    self.__project = None
    self.networkInterfaces = networkInterfaces
    self.metadata = metadata
    self.disks = disks
    self.machineType = machineType
    self.serviceAccounts = serviceAccounts
    self.tags = tags
    self.image = image
    self.zone = zone
    self.description = description
    self.name = name
    self.creationTimestamp = None
    self.id = None
    self.selfLink = None
    self.status = None
    self.statusMessage = None

  def __str__(self):
    return '<Instance instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(Instance.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#instance':
      raise ValueError('Cannot load Instance from {0}.'.format(kind))

    result = Instance(
        NetworkInterface.array_from_json(resource.get('networkInterfaces'), gce),
        Metadata.from_json(resource.get('metadata'), gce),
        AttachedDisk.array_from_json(resource.get('disks'), gce),
        resource.get('machineType'),
        ServiceAccount.array_from_json(resource.get('serviceAccounts'), gce),
        gce_base.GoogleComputeEngineBase._json_to_strings(resource.get('tags')),
        resource.get('image'),
        resource.get('zone'),
        resource.get('description'),
        resource.get('name'))

    result.creationTimestamp = resource.get('creationTimestamp')
    result.id = resource.get('id')
    self_link = resource.get('selfLink')
    result.selfLink = self_link
    result.status = resource.get('status')
    result.statusMessage = resource.get('statusMessage')
    result.__gce = gce
    result.__project = gce_base.GoogleComputeEngineBase._parse_project(self_link)
    return result

  @staticmethod
  def to_json(value, gce=None, project=None):
    result = {'kind': 'compute#instance'}
    if isinstance(value, Instance):
      if value.networkInterfaces is not None:
        result['networkInterfaces'] = NetworkInterface.array_to_json(value.networkInterfaces, gce, project)
      if value.metadata is not None:
        result['metadata'] = Metadata.to_json(value.metadata)
      if value.disks is not None:
        result['disks'] = AttachedDisk.array_to_json(value.disks, gce, project)
      if value.machineType is not None:
        result['machineType'] = (gce._normalize(project, 'machine-types', value.machineType) if (gce is not None and project is not None) else value.machineType)
      if value.serviceAccounts is not None:
        result['serviceAccounts'] = ServiceAccount.array_to_json(value.serviceAccounts)
      if value.tags is not None:
        result['tags'] = gce_base.GoogleComputeEngineBase._strings_to_json(value.tags)
      if value.image is not None:
        result['image'] = (gce._normalize(project, 'images', value.image) if (gce is not None and project is not None) else value.image)
      if value.zone is not None:
        result['zone'] = (gce._normalize(project, 'zones', value.zone) if (gce is not None and project is not None) else value.zone)
      if value.description is not None:
        result['description'] = value.description
      if value.name is not None:
        result['name'] = value.name
      if value.creationTimestamp is not None:
        result['creationTimestamp'] = value.creationTimestamp
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
      if value.status is not None:
        result['status'] = value.status
      if value.statusMessage is not None:
        result['statusMessage'] = value.statusMessage
    elif isinstance(value, dict):
      temp = value.get('networkInterfaces')
      if temp is not None:
        result['networkInterfaces'] = NetworkInterface.array_to_json(temp, gce, project)
      temp = value.get('metadata')
      if temp is not None:
        result['metadata'] = Metadata.to_json(temp)
      temp = value.get('disks')
      if temp is not None:
        result['disks'] = AttachedDisk.array_to_json(temp, gce, project)
      temp = value.get('machineType')
      if temp is not None:
        result['machineType'] = (gce._normalize(project, 'machine-types', temp) if (gce is not None and project is not None) else temp)
      temp = value.get('serviceAccounts')
      if temp is not None:
        result['serviceAccounts'] = ServiceAccount.array_to_json(temp)
      temp = value.get('tags')
      if temp is not None:
        result['tags'] = gce_base.GoogleComputeEngineBase._strings_to_json(temp)
      temp = value.get('image')
      if temp is not None:
        result['image'] = (gce._normalize(project, 'images', temp) if (gce is not None and project is not None) else temp)
      temp = value.get('zone')
      if temp is not None:
        result['zone'] = (gce._normalize(project, 'zones', temp) if (gce is not None and project is not None) else temp)
      temp = value.get('description')
      if temp is not None:
        result['description'] = temp
      temp = value.get('name')
      if temp is not None:
        result['name'] = temp
      temp = value.get('creationTimestamp')
      if temp is not None:
        result['creationTimestamp'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
      temp = value.get('status')
      if temp is not None:
        result['status'] = temp
      temp = value.get('statusMessage')
      if temp is not None:
        result['statusMessage'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [Instance.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value, gce, project):
    if value is None:
      return []
    elif isinstance(value, list):
      return [Instance.to_json(item, gce, project) for item in value]
    elif isinstance(value, dict) or isinstance(value, Instance):
      return [Instance.to_json(value, gce, project)]

  def insert(self, networkInterfaces=None, metadata=None, disks=None, machineType=None, serviceAccounts=None, tags=None, image=None, zone=None, description=None, name=None, project=None, blocking=True, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.insert_instance(self, networkInterfaces, metadata, disks, machineType, serviceAccounts, tags, image, zone, description, name, project, blocking)

  def get(self, project=None, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.get_instance(self, project)

  def delete(self, project=None, blocking=True, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.delete_instance(self, project, blocking)


class InstanceList(gce_base.ListObjectBase):
  """Generated class InstanceList."""
  __slots__ = ['items', 'nextPageToken', 'id', 'selfLink']

  def __init__(self, items=None, nextPageToken=None):
    gce_base.ListObjectBase.__init__(self, items)
    self.items = items
    self.nextPageToken = nextPageToken
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<InstanceList instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(InstanceList.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#instanceList':
      raise ValueError('Cannot load InstanceList from {0}.'.format(kind))

    result = InstanceList(
        Instance.array_from_json(resource.get('items'), gce),
        resource.get('nextPageToken'))

    result.id = resource.get('id')
    result.selfLink = resource.get('selfLink')
    return result

  @staticmethod
  def to_json(value, gce=None, project=None):
    result = {'kind': 'compute#instanceList'}
    if isinstance(value, InstanceList):
      if value.items is not None:
        result['items'] = Instance.array_to_json(value.items, gce, project)
      if value.nextPageToken is not None:
        result['nextPageToken'] = value.nextPageToken
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('items')
      if temp is not None:
        result['items'] = Instance.array_to_json(temp, gce, project)
      temp = value.get('nextPageToken')
      if temp is not None:
        result['nextPageToken'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result


class Kernel(object):
  """Generated class Kernel."""
  __slots__ = ['description', 'name', 'creationTimestamp', 'id', 'selfLink', '__gce', '__project']

  def __init__(self, description=None, name=None):
    self.__gce = None
    self.__project = None
    self.description = description
    self.name = name
    self.creationTimestamp = None
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<Kernel instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(Kernel.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#kernel':
      raise ValueError('Cannot load Kernel from {0}.'.format(kind))

    result = Kernel(
        resource.get('description'),
        resource.get('name'))

    result.creationTimestamp = resource.get('creationTimestamp')
    result.id = resource.get('id')
    self_link = resource.get('selfLink')
    result.selfLink = self_link
    result.__gce = gce
    result.__project = gce_base.GoogleComputeEngineBase._parse_project(self_link)
    return result

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#kernel'}
    if isinstance(value, Kernel):
      if value.description is not None:
        result['description'] = value.description
      if value.name is not None:
        result['name'] = value.name
      if value.creationTimestamp is not None:
        result['creationTimestamp'] = value.creationTimestamp
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('description')
      if temp is not None:
        result['description'] = temp
      temp = value.get('name')
      if temp is not None:
        result['name'] = temp
      temp = value.get('creationTimestamp')
      if temp is not None:
        result['creationTimestamp'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [Kernel.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value):
    if value is None:
      return []
    elif isinstance(value, list):
      return [Kernel.to_json(item) for item in value]
    elif isinstance(value, dict) or isinstance(value, Kernel):
      return [Kernel.to_json(value)]

  def get(self, project=None, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.get_kernel(self, project)


class KernelList(gce_base.ListObjectBase):
  """Generated class KernelList."""
  __slots__ = ['items', 'nextPageToken', 'id', 'selfLink']

  def __init__(self, items=None, nextPageToken=None):
    gce_base.ListObjectBase.__init__(self, items)
    self.items = items
    self.nextPageToken = nextPageToken
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<KernelList instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(KernelList.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#kernelList':
      raise ValueError('Cannot load KernelList from {0}.'.format(kind))

    result = KernelList(
        Kernel.array_from_json(resource.get('items'), gce),
        resource.get('nextPageToken'))

    result.id = resource.get('id')
    result.selfLink = resource.get('selfLink')
    return result

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#kernelList'}
    if isinstance(value, KernelList):
      if value.items is not None:
        result['items'] = Kernel.array_to_json(value.items)
      if value.nextPageToken is not None:
        result['nextPageToken'] = value.nextPageToken
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('items')
      if temp is not None:
        result['items'] = Kernel.array_to_json(temp)
      temp = value.get('nextPageToken')
      if temp is not None:
        result['nextPageToken'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result


class MachineType(object):
  """Generated class MachineType."""
  __slots__ = ['availableZone', 'description', 'ephemeralDisks', 'guestCpus', 'hostCpus', 'imageSpaceGb', 'maximumPersistentDisks', 'maximumPersistentDisksSizeGb', 'memoryMb', 'name', 'creationTimestamp', 'id', 'selfLink', '__gce', '__project']

  def __init__(self, availableZone=None, description=None, ephemeralDisks=None, guestCpus=None, hostCpus=None, imageSpaceGb=None, maximumPersistentDisks=None, maximumPersistentDisksSizeGb=None, memoryMb=None, name=None):
    self.__gce = None
    self.__project = None
    self.availableZone = availableZone
    self.description = description
    self.ephemeralDisks = ephemeralDisks
    self.guestCpus = guestCpus
    self.hostCpus = hostCpus
    self.imageSpaceGb = imageSpaceGb
    self.maximumPersistentDisks = maximumPersistentDisks
    self.maximumPersistentDisksSizeGb = maximumPersistentDisksSizeGb
    self.memoryMb = memoryMb
    self.name = name
    self.creationTimestamp = None
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<MachineType instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(MachineType.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#machineType':
      raise ValueError('Cannot load MachineType from {0}.'.format(kind))

    result = MachineType(
        gce_base.GoogleComputeEngineBase._json_to_strings(resource.get('availableZone')),
        resource.get('description'),
        _EphemeralDisk.array_from_json(resource.get('ephemeralDisks'), gce),
        resource.get('guestCpus'),
        resource.get('hostCpus'),
        resource.get('imageSpaceGb'),
        resource.get('maximumPersistentDisks'),
        resource.get('maximumPersistentDisksSizeGb'),
        resource.get('memoryMb'),
        resource.get('name'))

    result.creationTimestamp = resource.get('creationTimestamp')
    result.id = resource.get('id')
    self_link = resource.get('selfLink')
    result.selfLink = self_link
    result.__gce = gce
    result.__project = gce_base.GoogleComputeEngineBase._parse_project(self_link)
    return result

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#machineType'}
    if isinstance(value, MachineType):
      if value.availableZone is not None:
        result['availableZone'] = gce_base.GoogleComputeEngineBase._strings_to_json(value.availableZone)
      if value.description is not None:
        result['description'] = value.description
      if value.ephemeralDisks is not None:
        result['ephemeralDisks'] = _EphemeralDisk.array_to_json(value.ephemeralDisks)
      if value.guestCpus is not None:
        result['guestCpus'] = value.guestCpus
      if value.hostCpus is not None:
        result['hostCpus'] = value.hostCpus
      if value.imageSpaceGb is not None:
        result['imageSpaceGb'] = value.imageSpaceGb
      if value.maximumPersistentDisks is not None:
        result['maximumPersistentDisks'] = value.maximumPersistentDisks
      if value.maximumPersistentDisksSizeGb is not None:
        result['maximumPersistentDisksSizeGb'] = value.maximumPersistentDisksSizeGb
      if value.memoryMb is not None:
        result['memoryMb'] = value.memoryMb
      if value.name is not None:
        result['name'] = value.name
      if value.creationTimestamp is not None:
        result['creationTimestamp'] = value.creationTimestamp
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('availableZone')
      if temp is not None:
        result['availableZone'] = gce_base.GoogleComputeEngineBase._strings_to_json(temp)
      temp = value.get('description')
      if temp is not None:
        result['description'] = temp
      temp = value.get('ephemeralDisks')
      if temp is not None:
        result['ephemeralDisks'] = _EphemeralDisk.array_to_json(temp)
      temp = value.get('guestCpus')
      if temp is not None:
        result['guestCpus'] = temp
      temp = value.get('hostCpus')
      if temp is not None:
        result['hostCpus'] = temp
      temp = value.get('imageSpaceGb')
      if temp is not None:
        result['imageSpaceGb'] = temp
      temp = value.get('maximumPersistentDisks')
      if temp is not None:
        result['maximumPersistentDisks'] = temp
      temp = value.get('maximumPersistentDisksSizeGb')
      if temp is not None:
        result['maximumPersistentDisksSizeGb'] = temp
      temp = value.get('memoryMb')
      if temp is not None:
        result['memoryMb'] = temp
      temp = value.get('name')
      if temp is not None:
        result['name'] = temp
      temp = value.get('creationTimestamp')
      if temp is not None:
        result['creationTimestamp'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [MachineType.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value):
    if value is None:
      return []
    elif isinstance(value, list):
      return [MachineType.to_json(item) for item in value]
    elif isinstance(value, dict) or isinstance(value, MachineType):
      return [MachineType.to_json(value)]

  def get(self, project=None, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.get_machine_type(self, project)


class MachineTypeList(gce_base.ListObjectBase):
  """Generated class MachineTypeList."""
  __slots__ = ['items', 'nextPageToken', 'id', 'selfLink']

  def __init__(self, items=None, nextPageToken=None):
    gce_base.ListObjectBase.__init__(self, items)
    self.items = items
    self.nextPageToken = nextPageToken
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<MachineTypeList instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(MachineTypeList.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#machineTypeList':
      raise ValueError('Cannot load MachineTypeList from {0}.'.format(kind))

    result = MachineTypeList(
        MachineType.array_from_json(resource.get('items'), gce),
        resource.get('nextPageToken'))

    result.id = resource.get('id')
    result.selfLink = resource.get('selfLink')
    return result

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#machineTypeList'}
    if isinstance(value, MachineTypeList):
      if value.items is not None:
        result['items'] = MachineType.array_to_json(value.items)
      if value.nextPageToken is not None:
        result['nextPageToken'] = value.nextPageToken
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('items')
      if temp is not None:
        result['items'] = MachineType.array_to_json(temp)
      temp = value.get('nextPageToken')
      if temp is not None:
        result['nextPageToken'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result


class Metadata(object):
  """Generated class Metadata."""
  __slots__ = ['items']

  def __init__(self, items=None):
    self.items = items

  def __str__(self):
    return '<Metadata instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(Metadata.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#metadata':
      raise ValueError('Cannot load Metadata from {0}.'.format(kind))

    return Metadata(
        _Item.array_from_json(resource.get('items'), gce))

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#metadata'}
    if isinstance(value, Metadata):
      if value.items is not None:
        result['items'] = _Item.array_to_json(value.items)
    elif isinstance(value, dict):
      temp = value.get('items')
      if temp is not None:
        result['items'] = _Item.array_to_json(temp)
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result


class Network(object):
  """Generated class Network."""
  __slots__ = ['IPv4Range', 'gatewayIPv4', 'description', 'name', 'creationTimestamp', 'id', 'selfLink', '__gce', '__project']

  def __init__(self, IPv4Range=None, gatewayIPv4=None, description=None, name=None):
    self.__gce = None
    self.__project = None
    self.IPv4Range = IPv4Range
    self.gatewayIPv4 = gatewayIPv4
    self.description = description
    self.name = name
    self.creationTimestamp = None
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<Network instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(Network.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#network':
      raise ValueError('Cannot load Network from {0}.'.format(kind))

    result = Network(
        resource.get('IPv4Range'),
        resource.get('gatewayIPv4'),
        resource.get('description'),
        resource.get('name'))

    result.creationTimestamp = resource.get('creationTimestamp')
    result.id = resource.get('id')
    self_link = resource.get('selfLink')
    result.selfLink = self_link
    result.__gce = gce
    result.__project = gce_base.GoogleComputeEngineBase._parse_project(self_link)
    return result

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#network'}
    if isinstance(value, Network):
      if value.IPv4Range is not None:
        result['IPv4Range'] = value.IPv4Range
      if value.gatewayIPv4 is not None:
        result['gatewayIPv4'] = value.gatewayIPv4
      if value.description is not None:
        result['description'] = value.description
      if value.name is not None:
        result['name'] = value.name
      if value.creationTimestamp is not None:
        result['creationTimestamp'] = value.creationTimestamp
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('IPv4Range')
      if temp is not None:
        result['IPv4Range'] = temp
      temp = value.get('gatewayIPv4')
      if temp is not None:
        result['gatewayIPv4'] = temp
      temp = value.get('description')
      if temp is not None:
        result['description'] = temp
      temp = value.get('name')
      if temp is not None:
        result['name'] = temp
      temp = value.get('creationTimestamp')
      if temp is not None:
        result['creationTimestamp'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [Network.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value):
    if value is None:
      return []
    elif isinstance(value, list):
      return [Network.to_json(item) for item in value]
    elif isinstance(value, dict) or isinstance(value, Network):
      return [Network.to_json(value)]

  def insert(self, IPv4Range=None, gatewayIPv4=None, description=None, name=None, project=None, blocking=True, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.insert_network(self, IPv4Range, gatewayIPv4, description, name, project, blocking)

  def get(self, project=None, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.get_network(self, project)

  def delete(self, project=None, blocking=True, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.delete_network(self, project, blocking)


class NetworkInterface(object):
  """Generated class NetworkInterface."""
  __slots__ = ['network', 'accessConfigs', 'networkIP', 'name']

  def __init__(self, network=None, accessConfigs=None, networkIP=None):
    self.network = network
    self.accessConfigs = accessConfigs
    self.networkIP = networkIP
    self.name = None

  def __str__(self):
    return '<NetworkInterface instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(NetworkInterface.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#networkInterface':
      raise ValueError('Cannot load NetworkInterface from {0}.'.format(kind))

    result = NetworkInterface(
        resource.get('network'),
        AccessConfig.array_from_json(resource.get('accessConfigs'), gce),
        resource.get('networkIP'))

    result.name = resource.get('name')
    return result

  @staticmethod
  def to_json(value, gce=None, project=None):
    result = {'kind': 'compute#networkInterface'}
    if isinstance(value, NetworkInterface):
      if value.network is not None:
        result['network'] = (gce._normalize(project, 'networks', value.network) if (gce is not None and project is not None) else value.network)
      if value.accessConfigs is not None:
        result['accessConfigs'] = AccessConfig.array_to_json(value.accessConfigs)
      if value.networkIP is not None:
        result['networkIP'] = value.networkIP
      if value.name is not None:
        result['name'] = value.name
    elif isinstance(value, dict):
      temp = value.get('network')
      if temp is not None:
        result['network'] = (gce._normalize(project, 'networks', temp) if (gce is not None and project is not None) else temp)
      temp = value.get('accessConfigs')
      if temp is not None:
        result['accessConfigs'] = AccessConfig.array_to_json(temp)
      temp = value.get('networkIP')
      if temp is not None:
        result['networkIP'] = temp
      temp = value.get('name')
      if temp is not None:
        result['name'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [NetworkInterface.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value, gce, project):
    if value is None:
      return []
    elif isinstance(value, list):
      return [NetworkInterface.to_json(item, gce, project) for item in value]
    elif isinstance(value, dict) or isinstance(value, NetworkInterface):
      return [NetworkInterface.to_json(value, gce, project)]


class NetworkList(gce_base.ListObjectBase):
  """Generated class NetworkList."""
  __slots__ = ['items', 'nextPageToken', 'id', 'selfLink']

  def __init__(self, items=None, nextPageToken=None):
    gce_base.ListObjectBase.__init__(self, items)
    self.items = items
    self.nextPageToken = nextPageToken
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<NetworkList instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(NetworkList.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#networkList':
      raise ValueError('Cannot load NetworkList from {0}.'.format(kind))

    result = NetworkList(
        Network.array_from_json(resource.get('items'), gce),
        resource.get('nextPageToken'))

    result.id = resource.get('id')
    result.selfLink = resource.get('selfLink')
    return result

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#networkList'}
    if isinstance(value, NetworkList):
      if value.items is not None:
        result['items'] = Network.array_to_json(value.items)
      if value.nextPageToken is not None:
        result['nextPageToken'] = value.nextPageToken
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('items')
      if temp is not None:
        result['items'] = Network.array_to_json(temp)
      temp = value.get('nextPageToken')
      if temp is not None:
        result['nextPageToken'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result


class Operation(object):
  """Generated class Operation."""
  __slots__ = ['name', 'clientOperationId', 'creationTimestamp', 'endTime', 'errorErrors', 'httpErrorMessage', 'httpErrorStatusCode', 'id', 'insertTime', 'operationType', 'progress', 'selfLink', 'startTime', 'status', 'statusMessage', 'targetId', 'targetLink', 'user', '__gce', '__project']

  def __init__(self, name=None, errorErrors=None):
    self.__gce = None
    self.__project = None
    self.name = name
    self.clientOperationId = None
    self.creationTimestamp = None
    self.endTime = None
    self.errorErrors = errorErrors
    self.httpErrorMessage = None
    self.httpErrorStatusCode = None
    self.id = None
    self.insertTime = None
    self.operationType = None
    self.progress = None
    self.selfLink = None
    self.startTime = None
    self.status = None
    self.statusMessage = None
    self.targetId = None
    self.targetLink = None
    self.user = None

  def __str__(self):
    return '<Operation instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(Operation.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#operation':
      raise ValueError('Cannot load Operation from {0}.'.format(kind))

    errorErrors = None
    __temp = resource.get('error')
    if __temp is not None:
      errorErrors = _ErrorDetail.array_from_json(__temp.get('errors'), gce)
    result = Operation(
        resource.get('name'),
        errorErrors)

    result.clientOperationId = resource.get('clientOperationId')
    result.creationTimestamp = resource.get('creationTimestamp')
    result.endTime = resource.get('endTime')
    result.httpErrorMessage = resource.get('httpErrorMessage')
    result.httpErrorStatusCode = resource.get('httpErrorStatusCode')
    result.id = resource.get('id')
    result.insertTime = resource.get('insertTime')
    result.operationType = resource.get('operationType')
    result.progress = resource.get('progress')
    self_link = resource.get('selfLink')
    result.selfLink = self_link
    result.startTime = resource.get('startTime')
    result.status = resource.get('status')
    result.statusMessage = resource.get('statusMessage')
    result.targetId = resource.get('targetId')
    result.targetLink = resource.get('targetLink')
    result.user = resource.get('user')
    result.__gce = gce
    result.__project = gce_base.GoogleComputeEngineBase._parse_project(self_link)
    return result

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#operation'}
    if isinstance(value, Operation):
      if value.name is not None:
        result['name'] = value.name
      if value.clientOperationId is not None:
        result['clientOperationId'] = value.clientOperationId
      if value.creationTimestamp is not None:
        result['creationTimestamp'] = value.creationTimestamp
      if value.endTime is not None:
        result['endTime'] = value.endTime
      if value.errorErrors is not None:
        __temp = {}
        if value.errorErrors is not None:
          __temp['errors'] = _ErrorDetail.array_to_json(value.errorErrors)
        result['error'] = __temp
      if value.httpErrorMessage is not None:
        result['httpErrorMessage'] = value.httpErrorMessage
      if value.httpErrorStatusCode is not None:
        result['httpErrorStatusCode'] = value.httpErrorStatusCode
      if value.id is not None:
        result['id'] = value.id
      if value.insertTime is not None:
        result['insertTime'] = value.insertTime
      if value.operationType is not None:
        result['operationType'] = value.operationType
      if value.progress is not None:
        result['progress'] = value.progress
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
      if value.startTime is not None:
        result['startTime'] = value.startTime
      if value.status is not None:
        result['status'] = value.status
      if value.statusMessage is not None:
        result['statusMessage'] = value.statusMessage
      if value.targetId is not None:
        result['targetId'] = value.targetId
      if value.targetLink is not None:
        result['targetLink'] = value.targetLink
      if value.user is not None:
        result['user'] = value.user
    elif isinstance(value, dict):
      temp = value.get('name')
      if temp is not None:
        result['name'] = temp
      temp = value.get('clientOperationId')
      if temp is not None:
        result['clientOperationId'] = temp
      temp = value.get('creationTimestamp')
      if temp is not None:
        result['creationTimestamp'] = temp
      temp = value.get('endTime')
      if temp is not None:
        result['endTime'] = temp
      __temp = value.get('error')
      if __temp is not None:
        __temp_1 = {}
        temp = __temp.get('errors')
        if temp is not None:
          __temp_1['errors'] = _ErrorDetail.array_to_json(temp)
        result['error'] = __temp_1
      temp = value.get('httpErrorMessage')
      if temp is not None:
        result['httpErrorMessage'] = temp
      temp = value.get('httpErrorStatusCode')
      if temp is not None:
        result['httpErrorStatusCode'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('insertTime')
      if temp is not None:
        result['insertTime'] = temp
      temp = value.get('operationType')
      if temp is not None:
        result['operationType'] = temp
      temp = value.get('progress')
      if temp is not None:
        result['progress'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
      temp = value.get('startTime')
      if temp is not None:
        result['startTime'] = temp
      temp = value.get('status')
      if temp is not None:
        result['status'] = temp
      temp = value.get('statusMessage')
      if temp is not None:
        result['statusMessage'] = temp
      temp = value.get('targetId')
      if temp is not None:
        result['targetId'] = temp
      temp = value.get('targetLink')
      if temp is not None:
        result['targetLink'] = temp
      temp = value.get('user')
      if temp is not None:
        result['user'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [Operation.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value):
    if value is None:
      return []
    elif isinstance(value, list):
      return [Operation.to_json(item) for item in value]
    elif isinstance(value, dict) or isinstance(value, Operation):
      return [Operation.to_json(value)]

  def get(self, project=None, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.get_operation(self, project)

  def delete(self, project=None, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.delete_operation(self, project)


class OperationList(gce_base.ListObjectBase):
  """Generated class OperationList."""
  __slots__ = ['items', 'nextPageToken', 'id', 'selfLink']

  def __init__(self, items=None, nextPageToken=None):
    gce_base.ListObjectBase.__init__(self, items)
    self.items = items
    self.nextPageToken = nextPageToken
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<OperationList instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(OperationList.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#operationList':
      raise ValueError('Cannot load OperationList from {0}.'.format(kind))

    result = OperationList(
        Operation.array_from_json(resource.get('items'), gce),
        resource.get('nextPageToken'))

    result.id = resource.get('id')
    result.selfLink = resource.get('selfLink')
    return result

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#operationList'}
    if isinstance(value, OperationList):
      if value.items is not None:
        result['items'] = Operation.array_to_json(value.items)
      if value.nextPageToken is not None:
        result['nextPageToken'] = value.nextPageToken
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('items')
      if temp is not None:
        result['items'] = Operation.array_to_json(temp)
      temp = value.get('nextPageToken')
      if temp is not None:
        result['nextPageToken'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result


class Project(object):
  """Generated class Project."""
  __slots__ = ['commonInstanceMetadata', 'description', 'externalIpAddresses', 'name', 'quotas', 'creationTimestamp', 'id', 'selfLink', '__gce', '__project']

  def __init__(self, commonInstanceMetadata=None, description=None, externalIpAddresses=None, name=None, quotas=None):
    self.__gce = None
    self.__project = None
    self.commonInstanceMetadata = commonInstanceMetadata
    self.description = description
    self.externalIpAddresses = externalIpAddresses
    self.name = name
    self.quotas = quotas
    self.creationTimestamp = None
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<Project instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(Project.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#project':
      raise ValueError('Cannot load Project from {0}.'.format(kind))

    result = Project(
        Metadata.from_json(resource.get('commonInstanceMetadata'), gce),
        resource.get('description'),
        gce_base.GoogleComputeEngineBase._json_to_strings(resource.get('externalIpAddresses')),
        resource.get('name'),
        _Quota.array_from_json(resource.get('quotas'), gce))

    result.creationTimestamp = resource.get('creationTimestamp')
    result.id = resource.get('id')
    self_link = resource.get('selfLink')
    result.selfLink = self_link
    result.__gce = gce
    result.__project = gce_base.GoogleComputeEngineBase._parse_project(self_link)
    return result

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#project'}
    if isinstance(value, Project):
      if value.commonInstanceMetadata is not None:
        result['commonInstanceMetadata'] = Metadata.to_json(value.commonInstanceMetadata)
      if value.description is not None:
        result['description'] = value.description
      if value.externalIpAddresses is not None:
        result['externalIpAddresses'] = gce_base.GoogleComputeEngineBase._strings_to_json(value.externalIpAddresses)
      if value.name is not None:
        result['name'] = value.name
      if value.quotas is not None:
        result['quotas'] = _Quota.array_to_json(value.quotas)
      if value.creationTimestamp is not None:
        result['creationTimestamp'] = value.creationTimestamp
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('commonInstanceMetadata')
      if temp is not None:
        result['commonInstanceMetadata'] = Metadata.to_json(temp)
      temp = value.get('description')
      if temp is not None:
        result['description'] = temp
      temp = value.get('externalIpAddresses')
      if temp is not None:
        result['externalIpAddresses'] = gce_base.GoogleComputeEngineBase._strings_to_json(temp)
      temp = value.get('name')
      if temp is not None:
        result['name'] = temp
      temp = value.get('quotas')
      if temp is not None:
        result['quotas'] = _Quota.array_to_json(temp)
      temp = value.get('creationTimestamp')
      if temp is not None:
        result['creationTimestamp'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  def set_common_instance_metadata(self, items=None, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    return gce.set_common_instance_metadata(self, items)

  def get(self, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    return gce.get_project(self)


class ServiceAccount(object):
  """Generated class ServiceAccount."""
  __slots__ = ['email', 'scopes']

  def __init__(self, email=None, scopes=None):
    self.email = email
    self.scopes = scopes

  def __str__(self):
    return '<ServiceAccount instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(ServiceAccount.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#serviceAccount':
      raise ValueError('Cannot load ServiceAccount from {0}.'.format(kind))

    return ServiceAccount(
        resource.get('email'),
        gce_base.GoogleComputeEngineBase._json_to_strings(resource.get('scopes')))

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#serviceAccount'}
    if isinstance(value, ServiceAccount):
      if value.email is not None:
        result['email'] = value.email
      if value.scopes is not None:
        result['scopes'] = gce_base.GoogleComputeEngineBase._strings_to_json(value.scopes)
    elif isinstance(value, dict):
      temp = value.get('email')
      if temp is not None:
        result['email'] = temp
      temp = value.get('scopes')
      if temp is not None:
        result['scopes'] = gce_base.GoogleComputeEngineBase._strings_to_json(temp)
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [ServiceAccount.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value):
    if value is None:
      return []
    elif isinstance(value, list):
      return [ServiceAccount.to_json(item) for item in value]
    elif isinstance(value, dict) or isinstance(value, ServiceAccount):
      return [ServiceAccount.to_json(value)]


class Snapshot(object):
  """Generated class Snapshot."""
  __slots__ = ['sourceDisk', 'description', 'name', 'sourceDiskId', 'creationTimestamp', 'diskSizeGb', 'id', 'selfLink', 'status', '__gce', '__project']

  def __init__(self, sourceDisk=None, description=None, name=None, sourceDiskId=None):
    self.__gce = None
    self.__project = None
    self.sourceDisk = sourceDisk
    self.description = description
    self.name = name
    self.sourceDiskId = sourceDiskId
    self.creationTimestamp = None
    self.diskSizeGb = None
    self.id = None
    self.selfLink = None
    self.status = None

  def __str__(self):
    return '<Snapshot instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(Snapshot.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#snapshot':
      raise ValueError('Cannot load Snapshot from {0}.'.format(kind))

    result = Snapshot(
        resource.get('sourceDisk'),
        resource.get('description'),
        resource.get('name'),
        resource.get('sourceDiskId'))

    result.creationTimestamp = resource.get('creationTimestamp')
    result.diskSizeGb = resource.get('diskSizeGb')
    result.id = resource.get('id')
    self_link = resource.get('selfLink')
    result.selfLink = self_link
    result.status = resource.get('status')
    result.__gce = gce
    result.__project = gce_base.GoogleComputeEngineBase._parse_project(self_link)
    return result

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#snapshot'}
    if isinstance(value, Snapshot):
      if value.sourceDisk is not None:
        result['sourceDisk'] = value.sourceDisk
      if value.description is not None:
        result['description'] = value.description
      if value.name is not None:
        result['name'] = value.name
      if value.sourceDiskId is not None:
        result['sourceDiskId'] = value.sourceDiskId
      if value.creationTimestamp is not None:
        result['creationTimestamp'] = value.creationTimestamp
      if value.diskSizeGb is not None:
        result['diskSizeGb'] = value.diskSizeGb
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
      if value.status is not None:
        result['status'] = value.status
    elif isinstance(value, dict):
      temp = value.get('sourceDisk')
      if temp is not None:
        result['sourceDisk'] = temp
      temp = value.get('description')
      if temp is not None:
        result['description'] = temp
      temp = value.get('name')
      if temp is not None:
        result['name'] = temp
      temp = value.get('sourceDiskId')
      if temp is not None:
        result['sourceDiskId'] = temp
      temp = value.get('creationTimestamp')
      if temp is not None:
        result['creationTimestamp'] = temp
      temp = value.get('diskSizeGb')
      if temp is not None:
        result['diskSizeGb'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
      temp = value.get('status')
      if temp is not None:
        result['status'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [Snapshot.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value):
    if value is None:
      return []
    elif isinstance(value, list):
      return [Snapshot.to_json(item) for item in value]
    elif isinstance(value, dict) or isinstance(value, Snapshot):
      return [Snapshot.to_json(value)]

  def insert(self, sourceDisk=None, description=None, name=None, project=None, sourceDiskId=None, blocking=True, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.insert_snapshot(self, sourceDisk, description, name, project, sourceDiskId, blocking)

  def get(self, project=None, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.get_snapshot(self, project)

  def delete(self, project=None, blocking=True, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.delete_snapshot(self, project, blocking)


class SnapshotList(gce_base.ListObjectBase):
  """Generated class SnapshotList."""
  __slots__ = ['items', 'nextPageToken', 'id', 'selfLink']

  def __init__(self, items=None, nextPageToken=None):
    gce_base.ListObjectBase.__init__(self, items)
    self.items = items
    self.nextPageToken = nextPageToken
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<SnapshotList instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(SnapshotList.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#snapshotList':
      raise ValueError('Cannot load SnapshotList from {0}.'.format(kind))

    result = SnapshotList(
        Snapshot.array_from_json(resource.get('items'), gce),
        resource.get('nextPageToken'))

    result.id = resource.get('id')
    result.selfLink = resource.get('selfLink')
    return result

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#snapshotList'}
    if isinstance(value, SnapshotList):
      if value.items is not None:
        result['items'] = Snapshot.array_to_json(value.items)
      if value.nextPageToken is not None:
        result['nextPageToken'] = value.nextPageToken
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('items')
      if temp is not None:
        result['items'] = Snapshot.array_to_json(temp)
      temp = value.get('nextPageToken')
      if temp is not None:
        result['nextPageToken'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result


class Zone(object):
  """Generated class Zone."""
  __slots__ = ['description', 'maintenanceWindows', 'name', 'status', 'availableMachineType', 'creationTimestamp', 'id', 'selfLink', '__gce', '__project']

  def __init__(self, description=None, maintenanceWindows=None, name=None, status=None):
    self.__gce = None
    self.__project = None
    self.description = description
    self.maintenanceWindows = maintenanceWindows
    self.name = name
    self.status = status
    self.availableMachineType = None
    self.creationTimestamp = None
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<Zone instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(Zone.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#zone':
      raise ValueError('Cannot load Zone from {0}.'.format(kind))

    result = Zone(
        resource.get('description'),
        _MaintenanceWindow.array_from_json(resource.get('maintenanceWindows'), gce),
        resource.get('name'),
        resource.get('status'))

    result.availableMachineType = gce_base.GoogleComputeEngineBase._json_to_strings(resource.get('availableMachineType'))
    result.creationTimestamp = resource.get('creationTimestamp')
    result.id = resource.get('id')
    self_link = resource.get('selfLink')
    result.selfLink = self_link
    result.__gce = gce
    result.__project = gce_base.GoogleComputeEngineBase._parse_project(self_link)
    return result

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#zone'}
    if isinstance(value, Zone):
      if value.description is not None:
        result['description'] = value.description
      if value.maintenanceWindows is not None:
        result['maintenanceWindows'] = _MaintenanceWindow.array_to_json(value.maintenanceWindows)
      if value.name is not None:
        result['name'] = value.name
      if value.status is not None:
        result['status'] = value.status
      if value.availableMachineType is not None:
        result['availableMachineType'] = gce_base.GoogleComputeEngineBase._strings_to_json(value.availableMachineType)
      if value.creationTimestamp is not None:
        result['creationTimestamp'] = value.creationTimestamp
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('description')
      if temp is not None:
        result['description'] = temp
      temp = value.get('maintenanceWindows')
      if temp is not None:
        result['maintenanceWindows'] = _MaintenanceWindow.array_to_json(temp)
      temp = value.get('name')
      if temp is not None:
        result['name'] = temp
      temp = value.get('status')
      if temp is not None:
        result['status'] = temp
      temp = value.get('availableMachineType')
      if temp is not None:
        result['availableMachineType'] = gce_base.GoogleComputeEngineBase._strings_to_json(temp)
      temp = value.get('creationTimestamp')
      if temp is not None:
        result['creationTimestamp'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [Zone.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value):
    if value is None:
      return []
    elif isinstance(value, list):
      return [Zone.to_json(item) for item in value]
    elif isinstance(value, dict) or isinstance(value, Zone):
      return [Zone.to_json(value)]

  def get(self, project=None, gce=None):
    if gce is None: gce = self.__gce
    if gce is None: raise ValueError('Missing gce')
    if project is None: project = self.__project
    if project is None: raise ValueError('Missing project')
    return gce.get_zone(self, project)


class ZoneList(gce_base.ListObjectBase):
  """Generated class ZoneList."""
  __slots__ = ['items', 'nextPageToken', 'id', 'selfLink']

  def __init__(self, items=None, nextPageToken=None):
    gce_base.ListObjectBase.__init__(self, items)
    self.items = items
    self.nextPageToken = nextPageToken
    self.id = None
    self.selfLink = None

  def __str__(self):
    return '<ZoneList instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(ZoneList.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    kind = resource.get('kind')
    if kind != 'compute#zoneList':
      raise ValueError('Cannot load ZoneList from {0}.'.format(kind))

    result = ZoneList(
        Zone.array_from_json(resource.get('items'), gce),
        resource.get('nextPageToken'))

    result.id = resource.get('id')
    result.selfLink = resource.get('selfLink')
    return result

  @staticmethod
  def to_json(value):
    result = {'kind': 'compute#zoneList'}
    if isinstance(value, ZoneList):
      if value.items is not None:
        result['items'] = Zone.array_to_json(value.items)
      if value.nextPageToken is not None:
        result['nextPageToken'] = value.nextPageToken
      if value.id is not None:
        result['id'] = value.id
      if value.selfLink is not None:
        result['selfLink'] = value.selfLink
    elif isinstance(value, dict):
      temp = value.get('items')
      if temp is not None:
        result['items'] = Zone.array_to_json(temp)
      temp = value.get('nextPageToken')
      if temp is not None:
        result['nextPageToken'] = temp
      temp = value.get('id')
      if temp is not None:
        result['id'] = temp
      temp = value.get('selfLink')
      if temp is not None:
        result['selfLink'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result


class _Allowed(object):
  """Generated class _Allowed."""
  __slots__ = ['IPProtocol', 'ports']

  def __init__(self, IPProtocol=None, ports=None):
    self.IPProtocol = IPProtocol
    self.ports = ports

  def __str__(self):
    return '<_Allowed instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(_Allowed.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    return _Allowed(
        resource.get('IPProtocol'),
        gce_base.GoogleComputeEngineBase._json_to_strings(resource.get('ports')))

  @staticmethod
  def to_json(value):
    result = {}
    if isinstance(value, _Allowed):
      if value.IPProtocol is not None:
        result['IPProtocol'] = value.IPProtocol
      if value.ports is not None:
        result['ports'] = gce_base.GoogleComputeEngineBase._strings_to_json(value.ports)
    elif isinstance(value, dict):
      temp = value.get('IPProtocol')
      if temp is not None:
        result['IPProtocol'] = temp
      temp = value.get('ports')
      if temp is not None:
        result['ports'] = gce_base.GoogleComputeEngineBase._strings_to_json(temp)
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [_Allowed.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value):
    if value is None:
      return []
    elif isinstance(value, list):
      return [_Allowed.to_json(item) for item in value]
    elif isinstance(value, dict) or isinstance(value, _Allowed):
      return [_Allowed.to_json(value)]


class _EphemeralDisk(object):
  """Generated class _EphemeralDisk."""
  __slots__ = ['diskGb']

  def __init__(self, diskGb=None):
    self.diskGb = diskGb

  def __str__(self):
    return '<_EphemeralDisk instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(_EphemeralDisk.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    return _EphemeralDisk(
        resource.get('diskGb'))

  @staticmethod
  def to_json(value):
    result = {}
    if isinstance(value, _EphemeralDisk):
      if value.diskGb is not None:
        result['diskGb'] = value.diskGb
    elif isinstance(value, dict):
      temp = value.get('diskGb')
      if temp is not None:
        result['diskGb'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [_EphemeralDisk.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value):
    if value is None:
      return []
    elif isinstance(value, list):
      return [_EphemeralDisk.to_json(item) for item in value]
    elif isinstance(value, dict) or isinstance(value, _EphemeralDisk):
      return [_EphemeralDisk.to_json(value)]


class _ErrorDetail(object):
  """Generated class _ErrorDetail."""
  __slots__ = ['code', 'location', 'message']

  def __init__(self, code=None, location=None, message=None):
    self.code = code
    self.location = location
    self.message = message

  def __str__(self):
    return '<_ErrorDetail instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(_ErrorDetail.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    return _ErrorDetail(
        resource.get('code'),
        resource.get('location'),
        resource.get('message'))

  @staticmethod
  def to_json(value):
    result = {}
    if isinstance(value, _ErrorDetail):
      if value.code is not None:
        result['code'] = value.code
      if value.location is not None:
        result['location'] = value.location
      if value.message is not None:
        result['message'] = value.message
    elif isinstance(value, dict):
      temp = value.get('code')
      if temp is not None:
        result['code'] = temp
      temp = value.get('location')
      if temp is not None:
        result['location'] = temp
      temp = value.get('message')
      if temp is not None:
        result['message'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [_ErrorDetail.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value):
    if value is None:
      return []
    elif isinstance(value, list):
      return [_ErrorDetail.to_json(item) for item in value]
    elif isinstance(value, dict) or isinstance(value, _ErrorDetail):
      return [_ErrorDetail.to_json(value)]


class _Item(object):
  """Generated class _Item."""
  __slots__ = ['key', 'value']

  def __init__(self, key=None, value=None):
    self.key = key
    self.value = value

  def __str__(self):
    return '<_Item instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(_Item.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    return _Item(
        resource.get('key'),
        resource.get('value'))

  @staticmethod
  def to_json(value):
    result = {}
    if isinstance(value, _Item):
      if value.key is not None:
        result['key'] = value.key
      if value.value is not None:
        result['value'] = value.value
    elif isinstance(value, dict):
      temp = value.get('key')
      if temp is not None:
        result['key'] = temp
      temp = value.get('value')
      if temp is not None:
        result['value'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [_Item.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value):
    if value is None:
      return []
    elif isinstance(value, list):
      return [_Item.to_json(item) for item in value]
    elif isinstance(value, dict) or isinstance(value, _Item):
      return [_Item.to_json(value)]


class _MaintenanceWindow(object):
  """Generated class _MaintenanceWindow."""
  __slots__ = ['beginTime', 'description', 'endTime', 'name']

  def __init__(self, beginTime=None, description=None, endTime=None, name=None):
    self.beginTime = beginTime
    self.description = description
    self.endTime = endTime
    self.name = name

  def __str__(self):
    return '<_MaintenanceWindow instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(_MaintenanceWindow.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    return _MaintenanceWindow(
        resource.get('beginTime'),
        resource.get('description'),
        resource.get('endTime'),
        resource.get('name'))

  @staticmethod
  def to_json(value):
    result = {}
    if isinstance(value, _MaintenanceWindow):
      if value.beginTime is not None:
        result['beginTime'] = value.beginTime
      if value.description is not None:
        result['description'] = value.description
      if value.endTime is not None:
        result['endTime'] = value.endTime
      if value.name is not None:
        result['name'] = value.name
    elif isinstance(value, dict):
      temp = value.get('beginTime')
      if temp is not None:
        result['beginTime'] = temp
      temp = value.get('description')
      if temp is not None:
        result['description'] = temp
      temp = value.get('endTime')
      if temp is not None:
        result['endTime'] = temp
      temp = value.get('name')
      if temp is not None:
        result['name'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [_MaintenanceWindow.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value):
    if value is None:
      return []
    elif isinstance(value, list):
      return [_MaintenanceWindow.to_json(item) for item in value]
    elif isinstance(value, dict) or isinstance(value, _MaintenanceWindow):
      return [_MaintenanceWindow.to_json(value)]


class _Quota(object):
  """Generated class _Quota."""
  __slots__ = ['limit', 'metric', 'usage']

  def __init__(self, limit=None, metric=None, usage=None):
    self.limit = limit
    self.metric = metric
    self.usage = usage

  def __str__(self):
    return '<_Quota instance at {0:#x}:\n{1}>'.format(
        id(self), json.dumps(_Quota.to_json(self), indent=2))

  __repr__ = __str__

  @staticmethod
  def from_json(resource, gce=None):
    if resource is None:
      return None
    return _Quota(
        resource.get('limit'),
        resource.get('metric'),
        resource.get('usage'))

  @staticmethod
  def to_json(value):
    result = {}
    if isinstance(value, _Quota):
      if value.limit is not None:
        result['limit'] = value.limit
      if value.metric is not None:
        result['metric'] = value.metric
      if value.usage is not None:
        result['usage'] = value.usage
    elif isinstance(value, dict):
      temp = value.get('limit')
      if temp is not None:
        result['limit'] = temp
      temp = value.get('metric')
      if temp is not None:
        result['metric'] = temp
      temp = value.get('usage')
      if temp is not None:
        result['usage'] = temp
    else:
      raise TypeError('Cannot serialize {0} to json.'.format(str(value)))
    return result

  @staticmethod
  def array_from_json(input, gce=None):
    if input is not None:
      return [_Quota.from_json(item, gce) for item in input]

  @staticmethod
  def array_to_json(value):
    if value is None:
      return []
    elif isinstance(value, list):
      return [_Quota.to_json(item) for item in value]
    elif isinstance(value, dict) or isinstance(value, _Quota):
      return [_Quota.to_json(value)]


class GoogleComputeEngine(gce_base.GoogleComputeEngineBase):
  """The Google Compute Engine Api class is not thread safe yet."""

  VERSION = 'v1beta12'
  BASE_URL = 'https://www.googleapis.com/compute/v1beta12/projects/'

  __slots__ = []

  __OBJECT_PARSERS = {
      'compute#accessConfig': AccessConfig.from_json,
      'compute#attachedDisk': AttachedDisk.from_json,
      'compute#disk': Disk.from_json,
      'compute#diskList': DiskList.from_json,
      'compute#firewall': Firewall.from_json,
      'compute#firewallList': FirewallList.from_json,
      'compute#image': Image.from_json,
      'compute#imageList': ImageList.from_json,
      'compute#instance': Instance.from_json,
      'compute#instanceList': InstanceList.from_json,
      'compute#kernel': Kernel.from_json,
      'compute#kernelList': KernelList.from_json,
      'compute#machineType': MachineType.from_json,
      'compute#machineTypeList': MachineTypeList.from_json,
      'compute#metadata': Metadata.from_json,
      'compute#network': Network.from_json,
      'compute#networkInterface': NetworkInterface.from_json,
      'compute#networkList': NetworkList.from_json,
      'compute#operation': Operation.from_json,
      'compute#operationList': OperationList.from_json,
      'compute#project': Project.from_json,
      'compute#serviceAccount': ServiceAccount.from_json,
      'compute#snapshot': Snapshot.from_json,
      'compute#snapshotList': SnapshotList.from_json,
      'compute#zone': Zone.from_json,
      'compute#zoneList': ZoneList.from_json,
      }

  def _get_parsers(self):
    return GoogleComputeEngine.__OBJECT_PARSERS

  def __build_get_operation_request(self, operation=None, project=None):
    # Unpacks operation if its type is Operation or dict.
    if isinstance(operation, Operation):
      operation = operation.name
    elif isinstance(operation, dict):
      operation = operation.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not operation:
      raise ValueError('operation is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/operations/' + str(operation), None, None)

  def get_operation(self, operation=None, project=None):
    """Retrieves the specified operation resource.

    Args:
      operation:
          Name of the operation resource to return.
          Or: Operation to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Operation or a JSON
          describing the resource.
      project:
          Name of the project scoping this request.

    Returns: Operation
    """
    return self._parse(self._execute(self.__build_get_operation_request(
        operation, project), False))

  def get_operations(self, operations=None, project=None):
    """Retrieves the specified operation resource. List operation.

    Args:
      operations:
          List of operations to get.
      project:
          Name of the project scoping this request.

    Returns: List of Operation objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_get_operation_request(operation, project)
        for operation in operations], False))

  def list_operations(self, filter=None, project=None, maxResults=None, pageToken=None):
    """Retrieves the list of operation resources contained within the
    specified project.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.
      maxResults:
          Optional. Maximum count of results to be returned. Maximum
          and default value is 100.
      pageToken:
          Optional. Tag returned by a previous list request truncated
          by maxResults. Used to continue a previous list request.

    Returns: OperationList
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    if maxResults:
      query_params['maxResults'] = maxResults
    if pageToken:
      query_params['pageToken'] = pageToken
    return self._parse(self._execute(gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/operations', query_params, None), False))

  def all_operations(self, filter=None, project=None):
    """Returns an iterator yielding all operations in a project that
    match specified criteria.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.

    Returns: A generator of all operations.
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    return self._generate('GET', str(project) + '/operations', query_params, Operation)

  def __build_delete_operation_request(self, operation=None, project=None):
    # Unpacks operation if its type is Operation or dict.
    if isinstance(operation, Operation):
      operation = operation.name
    elif isinstance(operation, dict):
      operation = operation.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not operation:
      raise ValueError('operation is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('DELETE', str(project) + '/operations/' + str(operation), None, None)

  def delete_operation(self, operation=None, project=None):
    """Deletes the specified operation resource.

    Args:
      operation:
          Name of the operation resource to delete.
          Or: Operation to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Operation or a JSON
          describing the resource.
      project:
          Name of the project scoping this request.
    """
    return self._parse(self._execute(self.__build_delete_operation_request(
        operation, project), False))

  def delete_operations(self, operations=None, project=None):
    """Deletes the specified operation resource. List operation.

    Args:
      operations:
          List of operations to delete.
      project:
          Name of the project scoping this request.
    """
    return self._parse_list(self._execute_list([
        self.__build_delete_operation_request(operation, project)
        for operation in operations], False))

  def list_kernels(self, filter=None, project=None, maxResults=None, pageToken=None):
    """Retrieves the list of kernel resources available to the specified
    project.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.
      maxResults:
          Optional. Maximum count of results to be returned. Maximum
          and default value is 100.
      pageToken:
          Optional. Tag returned by a previous list request truncated
          by maxResults. Used to continue a previous list request.

    Returns: KernelList
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    if maxResults:
      query_params['maxResults'] = maxResults
    if pageToken:
      query_params['pageToken'] = pageToken
    return self._parse(self._execute(gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/kernels', query_params, None), False))

  def all_kernels(self, filter=None, project=None):
    """Returns an iterator yielding all kernels in a project that match
    specified criteria.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.

    Returns: A generator of all kernels.
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    return self._generate('GET', str(project) + '/kernels', query_params, Kernel)

  def __build_get_kernel_request(self, kernel=None, project=None):
    # Unpacks kernel if its type is Kernel or dict.
    if isinstance(kernel, Kernel):
      kernel = kernel.name
    elif isinstance(kernel, dict):
      kernel = kernel.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not kernel:
      raise ValueError('kernel is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/kernels/' + str(kernel), None, None)

  def get_kernel(self, kernel=None, project=None):
    """Returns the specified kernel resource.

    Args:
      kernel:
          Name of the kernel resource to return.
          Or: Kernel to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Kernel or a JSON describing
          the resource.
      project:
          Name of the project scoping this request.

    Returns: Kernel
    """
    return self._parse(self._execute(self.__build_get_kernel_request(
        kernel, project), False))

  def get_kernels(self, kernels=None, project=None):
    """Returns the specified kernel resource. List operation.

    Args:
      kernels:
          List of kernels to get.
      project:
          Name of the project scoping this request.

    Returns: List of Kernel objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_get_kernel_request(kernel, project)
        for kernel in kernels], False))

  def __build_insert_disk_request(self, disk=None, sizeGb=None, zone=None, description=None, name=None, project=None, sourceSnapshot=None, sourceSnapshotId=None, options=None, status=None, blocking=True):
    # Unpacks disk if its type is Disk or dict.
    if isinstance(disk, Disk):
      if sizeGb is None:
        sizeGb = disk.sizeGb
      if zone is None:
        zone = disk.zone
      if description is None:
        description = disk.description
      if name is None:
        name = disk.name
      if sourceSnapshot is None:
        sourceSnapshot = disk.sourceSnapshot
      if sourceSnapshotId is None:
        sourceSnapshotId = disk.sourceSnapshotId
      if options is None:
        options = disk.options
      if status is None:
        status = disk.status
    elif isinstance(disk, dict):
      if sizeGb is None:
        sizeGb = disk.get('sizeGb')
      if zone is None:
        zone = disk.get('zone')
      if description is None:
        description = disk.get('description')
      if name is None:
        name = disk.get('name')
      if sourceSnapshot is None:
        sourceSnapshot = disk.get('sourceSnapshot')
      if sourceSnapshotId is None:
        sourceSnapshotId = disk.get('sourceSnapshotId')
      if options is None:
        options = disk.get('options')
      if status is None:
        status = disk.get('status')
    elif isinstance(disk, basestring):
      if name is not None and disk != name:
        raise ValueError('Conflicting values of disk and name supplied.')
      name = disk

    # Applies global defaults to missing values.
    if zone is None:
      zone = self.default_zone
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not sizeGb:
      raise ValueError('sizeGb is a required parameter.')
    if not zone:
      raise ValueError('zone is a required parameter.')
    if not name:
      raise ValueError('name is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')

    # Creates a dict that will be sent in the request body.
    request = {
        'kind': 'compute#disk',
        'sizeGb': sizeGb,
        'zone': (self._normalize(project, 'zones', zone) if (self is not None and project is not None) else zone),
        'name': name
    }
    if description:
      request['description'] = description
    if sourceSnapshot:
      request['sourceSnapshot'] = sourceSnapshot
    if sourceSnapshotId:
      request['sourceSnapshotId'] = sourceSnapshotId
    if options:
      request['options'] = options
    if status:
      request['status'] = status
    return gce_base.GoogleComputeEngineBase.API_REQUEST('POST', str(project) + '/disks', None, json.dumps(request))

  def insert_disk(self, disk=None, sizeGb=None, zone=None, description=None, name=None, project=None, sourceSnapshot=None, sourceSnapshotId=None, options=None, status=None, blocking=True):
    """Creates a persistent disk resource in the specified project using
    the data included in the request.

    Args:
      disk:
          Disk to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Disk or a JSON describing
          the resource.
      sizeGb:
          Size of the persistent disk, specified in GB.
      zone:
          URL for the zone where the persistent disk resides;
          provided by the client when the disk is created. A
          persistent disk must reside in the same zone as the
          instance to which it is attached.
      description:
          An optional textual description of the resource; provided
          by the client when the resource is created.
      name:
          Name of the resource; provided by the client when the
          resource is created. The name must be 1-63 characters long,
          and comply with RFC1035.
      project:
          Name of the project scoping this request.
      sourceSnapshot:
          The source snapshot used to create this disk. Once the
          source snapshot has been deleted from the system, this
          field will be cleared, and will not be set even if a
          snapshot with the same name has been re-created.
      sourceSnapshotId:
          The 'id' value of the snapshot used to create this disk.
          This value may be used to determine whether the disk was
          created from the current or a previous instance of a given
          disk snapshot.
      options:
          Internal use only.
      status:
          The status of disk creation.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    return self._parse(self._execute(self.__build_insert_disk_request(
        disk, sizeGb, zone, description, name, project, sourceSnapshot, sourceSnapshotId, options, status, blocking), blocking))

  def insert_disks(self, disks=None, sizeGb=None, zone=None, description=None, names=None, project=None, sourceSnapshot=None, sourceSnapshotId=None, options=None, status=None, blocking=True):
    """Creates a persistent disk resource in the specified project using
    the data included in the request. List operation.

    Args:
      disks:
          List of disks to insert.
      sizeGb:
          Size of the persistent disk, specified in GB.
      zone:
          URL for the zone where the persistent disk resides;
          provided by the client when the disk is created. A
          persistent disk must reside in the same zone as the
          instance to which it is attached.
      description:
          An optional textual description of the resource; provided
          by the client when the resource is created.
      names:
          List of names of objects to insert.
      project:
          Name of the project scoping this request.
      sourceSnapshot:
          The source snapshot used to create this disk. Once the
          source snapshot has been deleted from the system, this
          field will be cleared, and will not be set even if a
          snapshot with the same name has been re-created.
      sourceSnapshotId:
          The 'id' value of the snapshot used to create this disk.
          This value may be used to determine whether the disk was
          created from the current or a previous instance of a given
          disk snapshot.
      options:
          Internal use only.
      status:
          The status of disk creation.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: List of Operation objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_insert_disk_request(disk, sizeGb, zone, description, name, project, sourceSnapshot, sourceSnapshotId, options, status, blocking)
        for disk, name in gce_base.GoogleComputeEngineBase._combine(disks, names)], blocking))

  def __build_get_disk_request(self, disk=None, project=None):
    # Unpacks disk if its type is Disk or dict.
    if isinstance(disk, Disk):
      disk = disk.name
    elif isinstance(disk, dict):
      disk = disk.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not disk:
      raise ValueError('disk is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/disks/' + str(disk), None, None)

  def get_disk(self, disk=None, project=None):
    """Returns the specified persistent disk resource.

    Args:
      disk:
          Name of the persistent disk resource to return.
          Or: Disk to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Disk or a JSON describing
          the resource.
      project:
          Name of the project scoping this request.

    Returns: Disk
    """
    return self._parse(self._execute(self.__build_get_disk_request(
        disk, project), False))

  def get_disks(self, disks=None, project=None):
    """Returns the specified persistent disk resource. List operation.

    Args:
      disks:
          List of disks to get.
      project:
          Name of the project scoping this request.

    Returns: List of Disk objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_get_disk_request(disk, project)
        for disk in disks], False))

  def list_disks(self, filter=None, project=None, maxResults=None, pageToken=None):
    """Retrieves the list of persistent disk resources contained within
    the specified project.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.
      maxResults:
          Optional. Maximum count of results to be returned. Maximum
          and default value is 100.
      pageToken:
          Optional. Tag returned by a previous list request truncated
          by maxResults. Used to continue a previous list request.

    Returns: DiskList
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    if maxResults:
      query_params['maxResults'] = maxResults
    if pageToken:
      query_params['pageToken'] = pageToken
    return self._parse(self._execute(gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/disks', query_params, None), False))

  def all_disks(self, filter=None, project=None):
    """Returns an iterator yielding all disks in a project that match
    specified criteria.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.

    Returns: A generator of all disks.
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    return self._generate('GET', str(project) + '/disks', query_params, Disk)

  def __build_delete_disk_request(self, disk=None, project=None, blocking=True):
    # Unpacks disk if its type is Disk or dict.
    if isinstance(disk, Disk):
      disk = disk.name
    elif isinstance(disk, dict):
      disk = disk.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not disk:
      raise ValueError('disk is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('DELETE', str(project) + '/disks/' + str(disk), None, None)

  def delete_disk(self, disk=None, project=None, blocking=True):
    """Deletes the specified persistent disk resource.

    Args:
      disk:
          Name of the persistent disk resource to delete.
          Or: Disk to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Disk or a JSON describing
          the resource.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    return self._parse(self._execute(self.__build_delete_disk_request(
        disk, project, blocking), blocking))

  def delete_disks(self, disks=None, project=None, blocking=True):
    """Deletes the specified persistent disk resource. List operation.

    Args:
      disks:
          List of disks to delete.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: List of Operation objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_delete_disk_request(disk, project, blocking)
        for disk in disks], blocking))

  def __build_insert_snapshot_request(self, snapshot=None, sourceDisk=None, description=None, name=None, project=None, sourceDiskId=None, blocking=True):
    # Unpacks snapshot if its type is Snapshot or dict.
    if isinstance(snapshot, Snapshot):
      if sourceDisk is None:
        sourceDisk = snapshot.sourceDisk
      if description is None:
        description = snapshot.description
      if name is None:
        name = snapshot.name
      if sourceDiskId is None:
        sourceDiskId = snapshot.sourceDiskId
    elif isinstance(snapshot, dict):
      if sourceDisk is None:
        sourceDisk = snapshot.get('sourceDisk')
      if description is None:
        description = snapshot.get('description')
      if name is None:
        name = snapshot.get('name')
      if sourceDiskId is None:
        sourceDiskId = snapshot.get('sourceDiskId')
    elif isinstance(snapshot, basestring):
      if name is not None and snapshot != name:
        raise ValueError('Conflicting values of snapshot and name supplied.')
      name = snapshot

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not name:
      raise ValueError('name is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')

    # Creates a dict that will be sent in the request body.
    request = {
        'kind': 'compute#snapshot',
        'name': name
    }
    if sourceDisk:
      request['sourceDisk'] = sourceDisk
    if description:
      request['description'] = description
    if sourceDiskId:
      request['sourceDiskId'] = sourceDiskId
    return gce_base.GoogleComputeEngineBase.API_REQUEST('POST', str(project) + '/snapshots', None, json.dumps(request))

  def insert_snapshot(self, snapshot=None, sourceDisk=None, description=None, name=None, project=None, sourceDiskId=None, blocking=True):
    """Creates a persistent disk snapshot resource in the specified
    project using the data included in the request.

    Args:
      snapshot:
          Snapshot to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Snapshot or a JSON
          describing the resource.
      sourceDisk:
          The source disk used to create this snapshot. Once the
          source disk has been deleted from the system, this field
          will be cleared, and will not be set even if a disk with
          the same name has been re-created.
      description:
          An optional textual description of the resource; provided
          by the client when the resource is created.
      name:
          Name of the resource; provided by the client when the
          resource is created. The name must be 1-63 characters long,
          and comply with RFC1035.
      project:
          Name of the project scoping this request.
      sourceDiskId:
          The 'id' value of the disk used to create this snapshot.
          This value may be used to determine whether the snapshot
          was taken from the current or a previous instance of a
          given disk name.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    return self._parse(self._execute(self.__build_insert_snapshot_request(
        snapshot, sourceDisk, description, name, project, sourceDiskId, blocking), blocking))

  def insert_snapshots(self, snapshots=None, sourceDisk=None, description=None, names=None, project=None, sourceDiskId=None, blocking=True):
    """Creates a persistent disk snapshot resource in the specified
    project using the data included in the request. List operation.

    Args:
      snapshots:
          List of snapshots to insert.
      sourceDisk:
          The source disk used to create this snapshot. Once the
          source disk has been deleted from the system, this field
          will be cleared, and will not be set even if a disk with
          the same name has been re-created.
      description:
          An optional textual description of the resource; provided
          by the client when the resource is created.
      names:
          List of names of objects to insert.
      project:
          Name of the project scoping this request.
      sourceDiskId:
          The 'id' value of the disk used to create this snapshot.
          This value may be used to determine whether the snapshot
          was taken from the current or a previous instance of a
          given disk name.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: List of Operation objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_insert_snapshot_request(snapshot, sourceDisk, description, name, project, sourceDiskId, blocking)
        for snapshot, name in gce_base.GoogleComputeEngineBase._combine(snapshots, names)], blocking))

  def __build_get_snapshot_request(self, snapshot=None, project=None):
    # Unpacks snapshot if its type is Snapshot or dict.
    if isinstance(snapshot, Snapshot):
      snapshot = snapshot.name
    elif isinstance(snapshot, dict):
      snapshot = snapshot.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not snapshot:
      raise ValueError('snapshot is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/snapshots/' + str(snapshot), None, None)

  def get_snapshot(self, snapshot=None, project=None):
    """Returns the specified persistent disk snapshot resource.

    Args:
      snapshot:
          Name of the persistent disk snapshot resource to return.
          Or: Snapshot to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Snapshot or a JSON
          describing the resource.
      project:
          Name of the project scoping this request.

    Returns: Snapshot
    """
    return self._parse(self._execute(self.__build_get_snapshot_request(
        snapshot, project), False))

  def get_snapshots(self, snapshots=None, project=None):
    """Returns the specified persistent disk snapshot resource. List
    operation.

    Args:
      snapshots:
          List of snapshots to get.
      project:
          Name of the project scoping this request.

    Returns: List of Snapshot objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_get_snapshot_request(snapshot, project)
        for snapshot in snapshots], False))

  def list_snapshots(self, filter=None, project=None, maxResults=None, pageToken=None):
    """Retrieves the list of persistent disk snapshot resources
    contained within the specified project.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.
      maxResults:
          Optional. Maximum count of results to be returned. Maximum
          and default value is 100.
      pageToken:
          Optional. Tag returned by a previous list request truncated
          by maxResults. Used to continue a previous list request.

    Returns: SnapshotList
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    if maxResults:
      query_params['maxResults'] = maxResults
    if pageToken:
      query_params['pageToken'] = pageToken
    return self._parse(self._execute(gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/snapshots', query_params, None), False))

  def all_snapshots(self, filter=None, project=None):
    """Returns an iterator yielding all snapshots in a project that
    match specified criteria.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.

    Returns: A generator of all snapshots.
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    return self._generate('GET', str(project) + '/snapshots', query_params, Snapshot)

  def __build_delete_snapshot_request(self, snapshot=None, project=None, blocking=True):
    # Unpacks snapshot if its type is Snapshot or dict.
    if isinstance(snapshot, Snapshot):
      snapshot = snapshot.name
    elif isinstance(snapshot, dict):
      snapshot = snapshot.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not snapshot:
      raise ValueError('snapshot is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('DELETE', str(project) + '/snapshots/' + str(snapshot), None, None)

  def delete_snapshot(self, snapshot=None, project=None, blocking=True):
    """Deletes the specified persistent disk snapshot resource.

    Args:
      snapshot:
          Name of the persistent disk snapshot resource to delete.
          Or: Snapshot to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Snapshot or a JSON
          describing the resource.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    return self._parse(self._execute(self.__build_delete_snapshot_request(
        snapshot, project, blocking), blocking))

  def delete_snapshots(self, snapshots=None, project=None, blocking=True):
    """Deletes the specified persistent disk snapshot resource. List
    operation.

    Args:
      snapshots:
          List of snapshots to delete.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: List of Operation objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_delete_snapshot_request(snapshot, project, blocking)
        for snapshot in snapshots], blocking))

  def list_zones(self, filter=None, project=None, maxResults=None, pageToken=None):
    """Retrieves the list of zone resources available to the specified
    project.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.
      maxResults:
          Optional. Maximum count of results to be returned. Maximum
          and default value is 100.
      pageToken:
          Optional. Tag returned by a previous list request truncated
          by maxResults. Used to continue a previous list request.

    Returns: ZoneList
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    if maxResults:
      query_params['maxResults'] = maxResults
    if pageToken:
      query_params['pageToken'] = pageToken
    return self._parse(self._execute(gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/zones', query_params, None), False))

  def all_zones(self, filter=None, project=None):
    """Returns an iterator yielding all zones in a project that match
    specified criteria.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.

    Returns: A generator of all zones.
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    return self._generate('GET', str(project) + '/zones', query_params, Zone)

  def __build_get_zone_request(self, zone=None, project=None):
    # Unpacks zone if its type is Zone or dict.
    if isinstance(zone, Zone):
      zone = zone.name
    elif isinstance(zone, dict):
      zone = zone.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not zone:
      raise ValueError('zone is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/zones/' + str(zone), None, None)

  def get_zone(self, zone=None, project=None):
    """Returns the specified zone resource.

    Args:
      zone:
          Name of the zone resource to return.
          Or: Zone to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Zone or a JSON describing
          the resource.
      project:
          Name of the project scoping this request.

    Returns: Zone
    """
    return self._parse(self._execute(self.__build_get_zone_request(
        zone, project), False))

  def get_zones(self, zones=None, project=None):
    """Returns the specified zone resource. List operation.

    Args:
      zones:
          List of zones to get.
      project:
          Name of the project scoping this request.

    Returns: List of Zone objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_get_zone_request(zone, project)
        for zone in zones], False))

  def __build_insert_instance_request(self, instance=None, networkInterfaces=None, metadata=None, disks=None, machineType=None, serviceAccounts=None, tags=None, image=None, zone=None, description=None, name=None, project=None, blocking=True):
    # Unpacks instance if its type is Instance or dict.
    if isinstance(instance, Instance):
      if networkInterfaces is None:
        networkInterfaces = instance.networkInterfaces
      if metadata is None:
        metadata = instance.metadata
      if disks is None:
        disks = instance.disks
      if machineType is None:
        machineType = instance.machineType
      if serviceAccounts is None:
        serviceAccounts = instance.serviceAccounts
      if tags is None:
        tags = instance.tags
      if image is None:
        image = instance.image
      if zone is None:
        zone = instance.zone
      if description is None:
        description = instance.description
      if name is None:
        name = instance.name
    elif isinstance(instance, dict):
      if networkInterfaces is None:
        networkInterfaces = instance.get('networkInterfaces')
      if metadata is None:
        metadata = instance.get('metadata')
      if disks is None:
        disks = instance.get('disks')
      if machineType is None:
        machineType = instance.get('machineType')
      if serviceAccounts is None:
        serviceAccounts = instance.get('serviceAccounts')
      if tags is None:
        tags = instance.get('tags')
      if image is None:
        image = instance.get('image')
      if zone is None:
        zone = instance.get('zone')
      if description is None:
        description = instance.get('description')
      if name is None:
        name = instance.get('name')
    elif isinstance(instance, basestring):
      if name is not None and instance != name:
        raise ValueError('Conflicting values of instance and name supplied.')
      name = instance

    # Applies global defaults to missing values.
    if networkInterfaces is None:
      networkInterfaces = self.default_network_interfaces
    if machineType is None:
      machineType = self.default_machine_type
    if image is None:
      image = self.default_image
    if zone is None:
      zone = self.default_zone
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not machineType:
      raise ValueError('machineType is a required parameter.')
    if not image:
      raise ValueError('image is a required parameter.')
    if not zone:
      raise ValueError('zone is a required parameter.')
    if not name:
      raise ValueError('name is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')

    # Creates a dict that will be sent in the request body.
    request = {
        'kind': 'compute#instance',
        'machineType': (self._normalize(project, 'machine-types', machineType) if (self is not None and project is not None) else machineType),
        'image': (self._normalize(project, 'images', image) if (self is not None and project is not None) else image),
        'zone': (self._normalize(project, 'zones', zone) if (self is not None and project is not None) else zone),
        'name': name
    }
    if networkInterfaces:
      request['networkInterfaces'] = NetworkInterface.array_to_json(networkInterfaces, self, project)
    if metadata:
      request['metadata'] = Metadata.to_json(metadata)
    if disks:
      request['disks'] = AttachedDisk.array_to_json(disks, self, project)
    if serviceAccounts:
      request['serviceAccounts'] = ServiceAccount.array_to_json(serviceAccounts)
    if tags:
      request['tags'] = gce_base.GoogleComputeEngineBase._strings_to_json(tags)
    if description:
      request['description'] = description
    return gce_base.GoogleComputeEngineBase.API_REQUEST('POST', str(project) + '/instances', None, json.dumps(request))

  def insert_instance(self, instance=None, networkInterfaces=None, metadata=None, disks=None, machineType=None, serviceAccounts=None, tags=None, image=None, zone=None, description=None, name=None, project=None, blocking=True):
    """Creates an instance resource in the specified project using the
    data included in the request.

    Args:
      instance:
          Instance to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Instance or a JSON
          describing the resource.
      networkInterfaces:
          Array of configurations for this interface. This specifies
          how this interface is configured to interact with other
          network services, such as connecting to the internet.
          Currently, ONE_TO_ONE_NAT is the only access config
          supported. If there are no accessConfigs specified, then
          this instance will have no external internet access.
      metadata:
          Metadata key/value pairs assigned to this instance.
          Consists of custom metadata or predefined keys; see
          Instance documentation for more information.
      disks:
          Array of disks associated with this instance. Persistent
          disks must be created before you can assign them.
      machineType:
          URL of the machine type resource describing which machine
          type to use to host the instance; provided by the client
          when the instance is created.
      serviceAccounts:
          A list of service accounts each with specified scopes, for
          which access tokens are to be made available to the
          instance through metadata queries.
      tags:
          An optional set of tags applied to this instance. Used to
          identify valid sources or targets for network firewalls.
          Provided by the client when the instance is created. Each
          tag must be 1-63 characters long, and comply with RFC1035.
      image:
          An optional URL of the disk image resource to be to be
          installed on this instance; provided by the client when the
          instance is created. If not specified, the server will
          choose a default image.
      zone:
          URL of the zone resource describing where this instance
          should be hosted; provided by the client when the instance
          is created.
      description:
          An optional textual description of the resource; provided
          by the client when the resource is created.
      name:
          Name of the resource; provided by the client when the
          resource is created. The name must be 1-63 characters long,
          and comply with RFC1035.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    return self._parse(self._execute(self.__build_insert_instance_request(
        instance, networkInterfaces, metadata, disks, machineType, serviceAccounts, tags, image, zone, description, name, project, blocking), blocking))

  def insert_instances(self, instances=None, networkInterfaces=None, metadata=None, disks=None, machineType=None, serviceAccounts=None, tags=None, image=None, zone=None, description=None, names=None, project=None, blocking=True):
    """Creates an instance resource in the specified project using the
    data included in the request. List operation.

    Args:
      instances:
          List of instances to insert.
      networkInterfaces:
          Array of configurations for this interface. This specifies
          how this interface is configured to interact with other
          network services, such as connecting to the internet.
          Currently, ONE_TO_ONE_NAT is the only access config
          supported. If there are no accessConfigs specified, then
          this instance will have no external internet access.
      metadata:
          Metadata key/value pairs assigned to this instance.
          Consists of custom metadata or predefined keys; see
          Instance documentation for more information.
      disks:
          Array of disks associated with this instance. Persistent
          disks must be created before you can assign them.
      machineType:
          URL of the machine type resource describing which machine
          type to use to host the instance; provided by the client
          when the instance is created.
      serviceAccounts:
          A list of service accounts each with specified scopes, for
          which access tokens are to be made available to the
          instance through metadata queries.
      tags:
          An optional set of tags applied to this instance. Used to
          identify valid sources or targets for network firewalls.
          Provided by the client when the instance is created. Each
          tag must be 1-63 characters long, and comply with RFC1035.
      image:
          An optional URL of the disk image resource to be to be
          installed on this instance; provided by the client when the
          instance is created. If not specified, the server will
          choose a default image.
      zone:
          URL of the zone resource describing where this instance
          should be hosted; provided by the client when the instance
          is created.
      description:
          An optional textual description of the resource; provided
          by the client when the resource is created.
      names:
          List of names of objects to insert.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: List of Operation objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_insert_instance_request(instance, networkInterfaces, metadata, disks, machineType, serviceAccounts, tags, image, zone, description, name, project, blocking)
        for instance, name in gce_base.GoogleComputeEngineBase._combine(instances, names)], blocking))

  def delete_access_config(self, instance=None, access_config=None, project=None, network_interface=None, blocking=True):
    """Deletes an access config from an instance's network interface.

    Args:
      instance:
          Instance name.
      access_config:
          Access config name.
      project:
          Project name.
      network_interface:
          Network interface name.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not instance:
      raise ValueError('instance is a required parameter.')
    if not access_config:
      raise ValueError('access_config is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    if not network_interface:
      raise ValueError('network_interface is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if access_config:
      query_params['access_config'] = access_config
    if network_interface:
      query_params['network_interface'] = network_interface
    return self._parse(self._execute(gce_base.GoogleComputeEngineBase.API_REQUEST('POST', str(project) + '/instances/' + str(instance) + '/delete-access-config', query_params, None), blocking))

  def __build_get_instance_request(self, instance=None, project=None):
    # Unpacks instance if its type is Instance or dict.
    if isinstance(instance, Instance):
      instance = instance.name
    elif isinstance(instance, dict):
      instance = instance.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not instance:
      raise ValueError('instance is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/instances/' + str(instance), None, None)

  def get_instance(self, instance=None, project=None):
    """Returns the specified instance resource.

    Args:
      instance:
          Name of the instance resource to return.
          Or: Instance to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Instance or a JSON
          describing the resource.
      project:
          Name of the project scoping this request.

    Returns: Instance
    """
    return self._parse(self._execute(self.__build_get_instance_request(
        instance, project), False))

  def get_instances(self, instances=None, project=None):
    """Returns the specified instance resource. List operation.

    Args:
      instances:
          List of instances to get.
      project:
          Name of the project scoping this request.

    Returns: List of Instance objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_get_instance_request(instance, project)
        for instance in instances], False))

  def list_instances(self, filter=None, project=None, maxResults=None, pageToken=None):
    """Retrieves the list of instance resources contained within the
    specified project.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.
      maxResults:
          Optional. Maximum count of results to be returned. Maximum
          and default value is 100.
      pageToken:
          Optional. Tag returned by a previous list request truncated
          by maxResults. Used to continue a previous list request.

    Returns: InstanceList
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    if maxResults:
      query_params['maxResults'] = maxResults
    if pageToken:
      query_params['pageToken'] = pageToken
    return self._parse(self._execute(gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/instances', query_params, None), False))

  def all_instances(self, filter=None, project=None):
    """Returns an iterator yielding all instances in a project that
    match specified criteria.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.

    Returns: A generator of all instances.
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    return self._generate('GET', str(project) + '/instances', query_params, Instance)

  def add_access_config(self, instance=None, name=None, project=None, network_interface=None, natIP=None, type=None, blocking=True):
    """Adds an access config to an instance's network interface.

    Args:
      instance:
          Instance name.
      name:
          Name of this access configuration.
      project:
          Project name.
      network_interface:
          Network interface name.
      natIP:
          An external IP address associated with this instance.
          Specify an unused static IP address available to the
          project. If left blank, the external IP will be drawn from
          a shared ephemeral pool.
      type:
          Type of configuration. Must be set to "ONE_TO_ONE_NAT".
          This configures port-for-port NAT to the internet.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not instance:
      raise ValueError('instance is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    if not network_interface:
      raise ValueError('network_interface is a required parameter.')

    # Creates a dict that will be sent in the request body.
    request = {
        'kind': 'compute#accessConfig'
    }
    if name:
      request['name'] = name
    if natIP:
      request['natIP'] = natIP
    if type:
      request['type'] = type

    # Processes the query parameters, if any.
    query_params = {}
    if network_interface:
      query_params['network_interface'] = network_interface
    return self._parse(self._execute(gce_base.GoogleComputeEngineBase.API_REQUEST('POST', str(project) + '/instances/' + str(instance) + '/add-access-config', query_params, json.dumps(request)), blocking))

  def __build_delete_instance_request(self, instance=None, project=None, blocking=True):
    # Unpacks instance if its type is Instance or dict.
    if isinstance(instance, Instance):
      instance = instance.name
    elif isinstance(instance, dict):
      instance = instance.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not instance:
      raise ValueError('instance is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('DELETE', str(project) + '/instances/' + str(instance), None, None)

  def delete_instance(self, instance=None, project=None, blocking=True):
    """Deletes the specified instance resource.

    Args:
      instance:
          Name of the instance resource to delete.
          Or: Instance to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Instance or a JSON
          describing the resource.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    return self._parse(self._execute(self.__build_delete_instance_request(
        instance, project, blocking), blocking))

  def delete_instances(self, instances=None, project=None, blocking=True):
    """Deletes the specified instance resource. List operation.

    Args:
      instances:
          List of instances to delete.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: List of Operation objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_delete_instance_request(instance, project, blocking)
        for instance in instances], blocking))

  def list_machine_types(self, filter=None, project=None, maxResults=None, pageToken=None):
    """Retrieves the list of machine type resources available to the
    specified project.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.
      maxResults:
          Optional. Maximum count of results to be returned. Maximum
          and default value is 100.
      pageToken:
          Optional. Tag returned by a previous list request truncated
          by maxResults. Used to continue a previous list request.

    Returns: MachineTypeList
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    if maxResults:
      query_params['maxResults'] = maxResults
    if pageToken:
      query_params['pageToken'] = pageToken
    return self._parse(self._execute(gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/machine-types', query_params, None), False))

  def all_machine_types(self, filter=None, project=None):
    """Returns an iterator yielding all machineTypes in a project that
    match specified criteria.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.

    Returns: A generator of all machineTypes.
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    return self._generate('GET', str(project) + '/machine-types', query_params, MachineType)

  def __build_get_machine_type_request(self, machineType=None, project=None):
    # Unpacks machineType if its type is MachineType or dict.
    if isinstance(machineType, MachineType):
      machineType = machineType.name
    elif isinstance(machineType, dict):
      machineType = machineType.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not machineType:
      raise ValueError('machineType is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/machine-types/' + str(machineType), None, None)

  def get_machine_type(self, machineType=None, project=None):
    """Returns the specified machine type resource.

    Args:
      machineType:
          Name of the machine type resource to return.
          Or: MachineType to use as a template. Other directly
          provided parameters take precedence and override any values
          in the template. May be an instance of MachineType or a
          JSON describing the resource.
      project:
          Name of the project scoping this request.

    Returns: MachineType
    """
    return self._parse(self._execute(self.__build_get_machine_type_request(
        machineType, project), False))

  def get_machine_types(self, machineTypes=None, project=None):
    """Returns the specified machine type resource. List operation.

    Args:
      machineTypes:
          List of machinetypes to get.
      project:
          Name of the project scoping this request.

    Returns: List of MachineType objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_get_machine_type_request(machineType, project)
        for machineType in machineTypes], False))

  def __build_insert_image_request(self, image=None, sourceType=None, rawDiskSource=None, rawDiskContainerType=None, description=None, name=None, rawDiskSha1Checksum=None, diskSnapshotSource=None, preferredKernel=None, project=None, blocking=True):
    # Unpacks image if its type is Image or dict.
    if isinstance(image, Image):
      if sourceType is None:
        sourceType = image.sourceType
      if rawDiskSource is None:
        rawDiskSource = image.rawDiskSource
      if rawDiskContainerType is None:
        rawDiskContainerType = image.rawDiskContainerType
      if description is None:
        description = image.description
      if name is None:
        name = image.name
      if rawDiskSha1Checksum is None:
        rawDiskSha1Checksum = image.rawDiskSha1Checksum
      if diskSnapshotSource is None:
        diskSnapshotSource = image.diskSnapshotSource
      if preferredKernel is None:
        preferredKernel = image.preferredKernel
    elif isinstance(image, dict):
      if sourceType is None:
        sourceType = image.get('sourceType')
      __temp = image.get('rawDisk')
      if __temp is not None:
        if containerType is None:
          containerType = __temp.get('containerType')
        if source is None:
          source = __temp.get('source')
        if sha1Checksum is None:
          sha1Checksum = __temp.get('sha1Checksum')
      if description is None:
        description = image.get('description')
      if name is None:
        name = image.get('name')
      __temp = image.get('diskSnapshot')
      if __temp is not None:
        if source is None:
          source = __temp.get('source')
      if preferredKernel is None:
        preferredKernel = image.get('preferredKernel')
    elif isinstance(image, basestring):
      if name is not None and image != name:
        raise ValueError('Conflicting values of image and name supplied.')
      name = image

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not sourceType:
      raise ValueError('sourceType is a required parameter.')
    if not name:
      raise ValueError('name is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')

    # Creates a dict that will be sent in the request body.
    request = {
        'kind': 'compute#image',
        'sourceType': sourceType,
        'name': name
    }
    if description:
      request['description'] = description
    if preferredKernel:
      request['preferredKernel'] = (self._normalize(project, 'kernels', preferredKernel) if (self is not None and project is not None) else preferredKernel)
    if rawDiskContainerType is not None or rawDiskSource is not None or rawDiskSha1Checksum is not None:
      if not rawDiskContainerType:
        raise ValueError('rawDiskContainerType is required parameter')
      if not rawDiskSource:
        raise ValueError('rawDiskSource is required parameter')
      __temp = {
          'containerType': rawDiskContainerType,
          'source': rawDiskSource
      }
      if sha1Checksum:
        __temp['sha1Checksum'] = rawDiskSha1Checksum
      request['rawDisk'] = __temp
    if diskSnapshotSource is not None:
      if not diskSnapshotSource:
        raise ValueError('diskSnapshotSource is required parameter')
      __temp = {
          'source': (self._normalize(project, 'disks', diskSnapshotSource) if (self is not None and project is not None) else diskSnapshotSource)
      }
      request['diskSnapshot'] = __temp
    return gce_base.GoogleComputeEngineBase.API_REQUEST('POST', str(project) + '/images', None, json.dumps(request))

  def insert_image(self, image=None, sourceType=None, rawDiskSource=None, rawDiskContainerType=None, description=None, name=None, rawDiskSha1Checksum=None, diskSnapshotSource=None, preferredKernel=None, project=None, blocking=True):
    """Creates an image resource in the specified project using the data
    included in the request.

    Args:
      image:
          Image to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Image or a JSON describing
          the resource.
      sourceType:
          Must be "RAW"; provided by the client when the disk image
          is created.
      rawDiskSource:
          The full Google Cloud Storage URL where the disk image is
          stored; provided by the client when the disk image is
          created.
      rawDiskContainerType:
          The format used to encode and transmit the block device.
          Should be TAR. This is just a container and transmission
          format and not a runtime format. Provided by the client
          when the disk image is created.
      description:
          Textual description of the resource; provided by the client
          when the resource is created.
      name:
          Name of the resource; provided by the client when the
          resource is created. The name must be 1-63 characters long,
          and comply with RFC1035.
      rawDiskSha1Checksum:
          An optional SHA1 checksum of the disk image before
          unpackaging; provided by the client when the disk image is
          created.
      diskSnapshotSource:
          URL of the disk snapshot.
      preferredKernel:
          An optional URL of the preferred kernel for use with this
          disk image. If not specified, a server defined default
          kernel will be used.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    return self._parse(self._execute(self.__build_insert_image_request(
        image, sourceType, rawDiskSource, rawDiskContainerType, description, name, rawDiskSha1Checksum, diskSnapshotSource, preferredKernel, project, blocking), blocking))

  def insert_images(self, images=None, sourceType=None, rawDiskSource=None, rawDiskContainerType=None, description=None, names=None, rawDiskSha1Checksum=None, diskSnapshotSource=None, preferredKernel=None, project=None, blocking=True):
    """Creates an image resource in the specified project using the data
    included in the request. List operation.

    Args:
      images:
          List of images to insert.
      sourceType:
          Must be "RAW"; provided by the client when the disk image
          is created.
      rawDiskSource:
          The full Google Cloud Storage URL where the disk image is
          stored; provided by the client when the disk image is
          created.
      rawDiskContainerType:
          The format used to encode and transmit the block device.
          Should be TAR. This is just a container and transmission
          format and not a runtime format. Provided by the client
          when the disk image is created.
      description:
          Textual description of the resource; provided by the client
          when the resource is created.
      names:
          List of names of objects to insert.
      rawDiskSha1Checksum:
          An optional SHA1 checksum of the disk image before
          unpackaging; provided by the client when the disk image is
          created.
      diskSnapshotSource:
          URL of the disk snapshot.
      preferredKernel:
          An optional URL of the preferred kernel for use with this
          disk image. If not specified, a server defined default
          kernel will be used.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: List of Operation objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_insert_image_request(image, sourceType, rawDiskSource, rawDiskContainerType, description, name, rawDiskSha1Checksum, diskSnapshotSource, preferredKernel, project, blocking)
        for image, name in gce_base.GoogleComputeEngineBase._combine(images, names)], blocking))

  def __build_get_image_request(self, image=None, project=None):
    # Unpacks image if its type is Image or dict.
    if isinstance(image, Image):
      image = image.name
    elif isinstance(image, dict):
      image = image.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not image:
      raise ValueError('image is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/images/' + str(image), None, None)

  def get_image(self, image=None, project=None):
    """Returns the specified image resource.

    Args:
      image:
          Name of the image resource to return.
          Or: Image to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Image or a JSON describing
          the resource.
      project:
          Name of the project scoping this request.

    Returns: Image
    """
    return self._parse(self._execute(self.__build_get_image_request(
        image, project), False))

  def get_images(self, images=None, project=None):
    """Returns the specified image resource. List operation.

    Args:
      images:
          List of images to get.
      project:
          Name of the project scoping this request.

    Returns: List of Image objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_get_image_request(image, project)
        for image in images], False))

  def list_images(self, filter=None, project=None, maxResults=None, pageToken=None):
    """Retrieves the list of image resources available to the specified
    project.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.
      maxResults:
          Optional. Maximum count of results to be returned. Maximum
          and default value is 100.
      pageToken:
          Optional. Tag returned by a previous list request truncated
          by maxResults. Used to continue a previous list request.

    Returns: ImageList
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    if maxResults:
      query_params['maxResults'] = maxResults
    if pageToken:
      query_params['pageToken'] = pageToken
    return self._parse(self._execute(gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/images', query_params, None), False))

  def all_images(self, filter=None, project=None):
    """Returns an iterator yielding all images in a project that match
    specified criteria.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.

    Returns: A generator of all images.
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    return self._generate('GET', str(project) + '/images', query_params, Image)

  def __build_delete_image_request(self, image=None, project=None, blocking=True):
    # Unpacks image if its type is Image or dict.
    if isinstance(image, Image):
      image = image.name
    elif isinstance(image, dict):
      image = image.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not image:
      raise ValueError('image is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('DELETE', str(project) + '/images/' + str(image), None, None)

  def delete_image(self, image=None, project=None, blocking=True):
    """Deletes the specified image resource.

    Args:
      image:
          Name of the image resource to delete.
          Or: Image to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Image or a JSON describing
          the resource.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    return self._parse(self._execute(self.__build_delete_image_request(
        image, project, blocking), blocking))

  def delete_images(self, images=None, project=None, blocking=True):
    """Deletes the specified image resource. List operation.

    Args:
      images:
          List of images to delete.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: List of Operation objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_delete_image_request(image, project, blocking)
        for image in images], blocking))

  def __build_insert_firewall_request(self, firewall=None, network=None, allowed=None, sourceRanges=None, sourceTags=None, targetTags=None, description=None, name=None, project=None, blocking=True):
    # Unpacks firewall if its type is Firewall or dict.
    if isinstance(firewall, Firewall):
      if network is None:
        network = firewall.network
      if allowed is None:
        allowed = firewall.allowed
      if sourceRanges is None:
        sourceRanges = firewall.sourceRanges
      if sourceTags is None:
        sourceTags = firewall.sourceTags
      if targetTags is None:
        targetTags = firewall.targetTags
      if description is None:
        description = firewall.description
      if name is None:
        name = firewall.name
    elif isinstance(firewall, dict):
      if network is None:
        network = firewall.get('network')
      if allowed is None:
        allowed = firewall.get('allowed')
      if sourceRanges is None:
        sourceRanges = firewall.get('sourceRanges')
      if sourceTags is None:
        sourceTags = firewall.get('sourceTags')
      if targetTags is None:
        targetTags = firewall.get('targetTags')
      if description is None:
        description = firewall.get('description')
      if name is None:
        name = firewall.get('name')
    elif isinstance(firewall, basestring):
      if name is not None and firewall != name:
        raise ValueError('Conflicting values of firewall and name supplied.')
      name = firewall

    # Applies global defaults to missing values.
    if network is None:
      network = self.default_network
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not network:
      raise ValueError('network is a required parameter.')
    if not name:
      raise ValueError('name is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')

    # Creates a dict that will be sent in the request body.
    request = {
        'kind': 'compute#firewall',
        'network': (self._normalize(project, 'networks', network) if (self is not None and project is not None) else network),
        'name': name
    }
    if allowed:
      request['allowed'] = _Allowed.array_to_json(allowed)
    if sourceRanges:
      request['sourceRanges'] = gce_base.GoogleComputeEngineBase._strings_to_json(sourceRanges)
    if sourceTags:
      request['sourceTags'] = gce_base.GoogleComputeEngineBase._strings_to_json(sourceTags)
    if targetTags:
      request['targetTags'] = gce_base.GoogleComputeEngineBase._strings_to_json(targetTags)
    if description:
      request['description'] = description
    return gce_base.GoogleComputeEngineBase.API_REQUEST('POST', str(project) + '/firewalls', None, json.dumps(request))

  def insert_firewall(self, firewall=None, network=None, allowed=None, sourceRanges=None, sourceTags=None, targetTags=None, description=None, name=None, project=None, blocking=True):
    """Creates a firewall resource in the specified project using the
    data included in the request.

    Args:
      firewall:
          Firewall to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Firewall or a JSON
          describing the resource.
      network:
          URL of the network to which this firewall is applied;
          provided by the client when the firewall is created.
      allowed:
          The list of rules specified by this firewall. Each rule
          specifies a protocol and port-range tuple that describes a
          permitted connection.
      sourceRanges:
          A list of IP address blocks expressed in CIDR format which
          this rule applies to. One or both of sourceRanges and
          sourceTags may be set; an inbound connection is allowed if
          either the range or the tag of the source matches.
      sourceTags:
          A list of instance tags which this rule applies to. One or
          both of sourceRanges and sourceTags may be set; an inbound
          connection is allowed if either the range or the tag of the
          source matches.
      targetTags:
          A list of instance tags indicating sets of instances
          located on network which may make network connections as
          specified in allowed. If no targetTags are specified, the
          firewall rule applies to all instances on the specified
          network.
      description:
          An optional textual description of the resource; provided
          by the client when the resource is created.
      name:
          Name of the resource; provided by the client when the
          resource is created. The name must be 1-63 characters long,
          and comply with RFC1035.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    return self._parse(self._execute(self.__build_insert_firewall_request(
        firewall, network, allowed, sourceRanges, sourceTags, targetTags, description, name, project, blocking), blocking))

  def insert_firewalls(self, firewalls=None, network=None, allowed=None, sourceRanges=None, sourceTags=None, targetTags=None, description=None, names=None, project=None, blocking=True):
    """Creates a firewall resource in the specified project using the
    data included in the request. List operation.

    Args:
      firewalls:
          List of firewalls to insert.
      network:
          URL of the network to which this firewall is applied;
          provided by the client when the firewall is created.
      allowed:
          The list of rules specified by this firewall. Each rule
          specifies a protocol and port-range tuple that describes a
          permitted connection.
      sourceRanges:
          A list of IP address blocks expressed in CIDR format which
          this rule applies to. One or both of sourceRanges and
          sourceTags may be set; an inbound connection is allowed if
          either the range or the tag of the source matches.
      sourceTags:
          A list of instance tags which this rule applies to. One or
          both of sourceRanges and sourceTags may be set; an inbound
          connection is allowed if either the range or the tag of the
          source matches.
      targetTags:
          A list of instance tags indicating sets of instances
          located on network which may make network connections as
          specified in allowed. If no targetTags are specified, the
          firewall rule applies to all instances on the specified
          network.
      description:
          An optional textual description of the resource; provided
          by the client when the resource is created.
      names:
          List of names of objects to insert.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: List of Operation objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_insert_firewall_request(firewall, network, allowed, sourceRanges, sourceTags, targetTags, description, name, project, blocking)
        for firewall, name in gce_base.GoogleComputeEngineBase._combine(firewalls, names)], blocking))

  def __build_get_firewall_request(self, firewall=None, project=None):
    # Unpacks firewall if its type is Firewall or dict.
    if isinstance(firewall, Firewall):
      firewall = firewall.name
    elif isinstance(firewall, dict):
      firewall = firewall.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not firewall:
      raise ValueError('firewall is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/firewalls/' + str(firewall), None, None)

  def get_firewall(self, firewall=None, project=None):
    """Returns the specified firewall resource.

    Args:
      firewall:
          Name of the firewall resource to return.
          Or: Firewall to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Firewall or a JSON
          describing the resource.
      project:
          Name of the project scoping this request.

    Returns: Firewall
    """
    return self._parse(self._execute(self.__build_get_firewall_request(
        firewall, project), False))

  def get_firewalls(self, firewalls=None, project=None):
    """Returns the specified firewall resource. List operation.

    Args:
      firewalls:
          List of firewalls to get.
      project:
          Name of the project scoping this request.

    Returns: List of Firewall objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_get_firewall_request(firewall, project)
        for firewall in firewalls], False))

  def list_firewalls(self, filter=None, project=None, maxResults=None, pageToken=None):
    """Retrieves the list of firewall resources available to the
    specified project.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.
      maxResults:
          Optional. Maximum count of results to be returned. Maximum
          and default value is 100.
      pageToken:
          Optional. Tag returned by a previous list request truncated
          by maxResults. Used to continue a previous list request.

    Returns: FirewallList
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    if maxResults:
      query_params['maxResults'] = maxResults
    if pageToken:
      query_params['pageToken'] = pageToken
    return self._parse(self._execute(gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/firewalls', query_params, None), False))

  def all_firewalls(self, filter=None, project=None):
    """Returns an iterator yielding all firewalls in a project that
    match specified criteria.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.

    Returns: A generator of all firewalls.
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    return self._generate('GET', str(project) + '/firewalls', query_params, Firewall)

  def __build_update_firewall_request(self, firewall=None, network=None, allowed=None, sourceRanges=None, sourceTags=None, targetTags=None, description=None, name=None, project=None, blocking=True):
    # Unpacks firewall if its type is Firewall or dict.
    if isinstance(firewall, Firewall):
      if network is None:
        network = firewall.network
      if allowed is None:
        allowed = firewall.allowed
      if sourceRanges is None:
        sourceRanges = firewall.sourceRanges
      if sourceTags is None:
        sourceTags = firewall.sourceTags
      if targetTags is None:
        targetTags = firewall.targetTags
      if description is None:
        description = firewall.description
      if name is None:
        name = firewall.name
      firewall = firewall.name
    elif isinstance(firewall, dict):
      if network is None:
        network = firewall.get('network')
      if allowed is None:
        allowed = firewall.get('allowed')
      if sourceRanges is None:
        sourceRanges = firewall.get('sourceRanges')
      if sourceTags is None:
        sourceTags = firewall.get('sourceTags')
      if targetTags is None:
        targetTags = firewall.get('targetTags')
      if description is None:
        description = firewall.get('description')
      if name is None:
        name = firewall.get('name')
      firewall = firewall.get('name')

    # Applies global defaults to missing values.
    if network is None:
      network = self.default_network
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not firewall:
      raise ValueError('firewall is a required parameter.')
    if not network:
      raise ValueError('network is a required parameter.')
    if not name:
      raise ValueError('name is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')

    # Creates a dict that will be sent in the request body.
    request = {
        'kind': 'compute#firewall',
        'network': (self._normalize(project, 'networks', network) if (self is not None and project is not None) else network),
        'name': name
    }
    if allowed:
      request['allowed'] = _Allowed.array_to_json(allowed)
    if sourceRanges:
      request['sourceRanges'] = gce_base.GoogleComputeEngineBase._strings_to_json(sourceRanges)
    if sourceTags:
      request['sourceTags'] = gce_base.GoogleComputeEngineBase._strings_to_json(sourceTags)
    if targetTags:
      request['targetTags'] = gce_base.GoogleComputeEngineBase._strings_to_json(targetTags)
    if description:
      request['description'] = description
    return gce_base.GoogleComputeEngineBase.API_REQUEST('PUT', str(project) + '/firewalls/' + str(firewall), None, json.dumps(request))

  def update_firewall(self, firewall=None, network=None, allowed=None, sourceRanges=None, sourceTags=None, targetTags=None, description=None, name=None, project=None, blocking=True):
    """Updates the specified firewall resource with the data included in
    the request.

    Args:
      firewall:
          Name of the firewall resource to update.
          Or: Firewall to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Firewall or a JSON
          describing the resource.
      network:
          URL of the network to which this firewall is applied;
          provided by the client when the firewall is created.
      allowed:
          The list of rules specified by this firewall. Each rule
          specifies a protocol and port-range tuple that describes a
          permitted connection.
      sourceRanges:
          A list of IP address blocks expressed in CIDR format which
          this rule applies to. One or both of sourceRanges and
          sourceTags may be set; an inbound connection is allowed if
          either the range or the tag of the source matches.
      sourceTags:
          A list of instance tags which this rule applies to. One or
          both of sourceRanges and sourceTags may be set; an inbound
          connection is allowed if either the range or the tag of the
          source matches.
      targetTags:
          A list of instance tags indicating sets of instances
          located on network which may make network connections as
          specified in allowed. If no targetTags are specified, the
          firewall rule applies to all instances on the specified
          network.
      description:
          An optional textual description of the resource; provided
          by the client when the resource is created.
      name:
          Name of the resource; provided by the client when the
          resource is created. The name must be 1-63 characters long,
          and comply with RFC1035.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    return self._parse(self._execute(self.__build_update_firewall_request(
        firewall, network, allowed, sourceRanges, sourceTags, targetTags, description, name, project, blocking), blocking))

  def update_firewalls(self, firewalls=None, network=None, allowed=None, sourceRanges=None, sourceTags=None, targetTags=None, description=None, names=None, project=None, blocking=True):
    """Updates the specified firewall resource with the data included in
    the request. List operation.

    Args:
      firewalls:
          List of firewalls to update.
      network:
          URL of the network to which this firewall is applied;
          provided by the client when the firewall is created.
      allowed:
          The list of rules specified by this firewall. Each rule
          specifies a protocol and port-range tuple that describes a
          permitted connection.
      sourceRanges:
          A list of IP address blocks expressed in CIDR format which
          this rule applies to. One or both of sourceRanges and
          sourceTags may be set; an inbound connection is allowed if
          either the range or the tag of the source matches.
      sourceTags:
          A list of instance tags which this rule applies to. One or
          both of sourceRanges and sourceTags may be set; an inbound
          connection is allowed if either the range or the tag of the
          source matches.
      targetTags:
          A list of instance tags indicating sets of instances
          located on network which may make network connections as
          specified in allowed. If no targetTags are specified, the
          firewall rule applies to all instances on the specified
          network.
      description:
          An optional textual description of the resource; provided
          by the client when the resource is created.
      names:
          List of names of objects to update.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: List of Operation objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_update_firewall_request(firewall, network, allowed, sourceRanges, sourceTags, targetTags, description, name, project, blocking)
        for firewall, name in gce_base.GoogleComputeEngineBase._combine(firewalls, names)], blocking))

  def __build_patch_firewall_request(self, firewall=None, network=None, allowed=None, sourceRanges=None, sourceTags=None, targetTags=None, description=None, name=None, project=None, blocking=True):
    # Unpacks firewall if its type is Firewall or dict.
    if isinstance(firewall, Firewall):
      if network is None:
        network = firewall.network
      if allowed is None:
        allowed = firewall.allowed
      if sourceRanges is None:
        sourceRanges = firewall.sourceRanges
      if sourceTags is None:
        sourceTags = firewall.sourceTags
      if targetTags is None:
        targetTags = firewall.targetTags
      if description is None:
        description = firewall.description
      if name is None:
        name = firewall.name
      firewall = firewall.name
    elif isinstance(firewall, dict):
      if network is None:
        network = firewall.get('network')
      if allowed is None:
        allowed = firewall.get('allowed')
      if sourceRanges is None:
        sourceRanges = firewall.get('sourceRanges')
      if sourceTags is None:
        sourceTags = firewall.get('sourceTags')
      if targetTags is None:
        targetTags = firewall.get('targetTags')
      if description is None:
        description = firewall.get('description')
      if name is None:
        name = firewall.get('name')
      firewall = firewall.get('name')

    # Applies global defaults to missing values.
    if network is None:
      network = self.default_network
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not firewall:
      raise ValueError('firewall is a required parameter.')
    if not network:
      raise ValueError('network is a required parameter.')
    if not name:
      raise ValueError('name is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')

    # Creates a dict that will be sent in the request body.
    request = {
        'kind': 'compute#firewall',
        'network': (self._normalize(project, 'networks', network) if (self is not None and project is not None) else network),
        'name': name
    }
    if allowed:
      request['allowed'] = _Allowed.array_to_json(allowed)
    if sourceRanges:
      request['sourceRanges'] = gce_base.GoogleComputeEngineBase._strings_to_json(sourceRanges)
    if sourceTags:
      request['sourceTags'] = gce_base.GoogleComputeEngineBase._strings_to_json(sourceTags)
    if targetTags:
      request['targetTags'] = gce_base.GoogleComputeEngineBase._strings_to_json(targetTags)
    if description:
      request['description'] = description
    return gce_base.GoogleComputeEngineBase.API_REQUEST('PATCH', str(project) + '/firewalls/' + str(firewall), None, json.dumps(request))

  def patch_firewall(self, firewall=None, network=None, allowed=None, sourceRanges=None, sourceTags=None, targetTags=None, description=None, name=None, project=None, blocking=True):
    """Updates the specified firewall resource with the data included in
    the request. This method supports patch semantics.

    Args:
      firewall:
          Name of the firewall resource to update.
          Or: Firewall to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Firewall or a JSON
          describing the resource.
      network:
          URL of the network to which this firewall is applied;
          provided by the client when the firewall is created.
      allowed:
          The list of rules specified by this firewall. Each rule
          specifies a protocol and port-range tuple that describes a
          permitted connection.
      sourceRanges:
          A list of IP address blocks expressed in CIDR format which
          this rule applies to. One or both of sourceRanges and
          sourceTags may be set; an inbound connection is allowed if
          either the range or the tag of the source matches.
      sourceTags:
          A list of instance tags which this rule applies to. One or
          both of sourceRanges and sourceTags may be set; an inbound
          connection is allowed if either the range or the tag of the
          source matches.
      targetTags:
          A list of instance tags indicating sets of instances
          located on network which may make network connections as
          specified in allowed. If no targetTags are specified, the
          firewall rule applies to all instances on the specified
          network.
      description:
          An optional textual description of the resource; provided
          by the client when the resource is created.
      name:
          Name of the resource; provided by the client when the
          resource is created. The name must be 1-63 characters long,
          and comply with RFC1035.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    return self._parse(self._execute(self.__build_patch_firewall_request(
        firewall, network, allowed, sourceRanges, sourceTags, targetTags, description, name, project, blocking), blocking))

  def patch_firewalls(self, firewalls=None, network=None, allowed=None, sourceRanges=None, sourceTags=None, targetTags=None, description=None, names=None, project=None, blocking=True):
    """Updates the specified firewall resource with the data included in
    the request. This method supports patch semantics. List operation.

    Args:
      firewalls:
          List of firewalls to patch.
      network:
          URL of the network to which this firewall is applied;
          provided by the client when the firewall is created.
      allowed:
          The list of rules specified by this firewall. Each rule
          specifies a protocol and port-range tuple that describes a
          permitted connection.
      sourceRanges:
          A list of IP address blocks expressed in CIDR format which
          this rule applies to. One or both of sourceRanges and
          sourceTags may be set; an inbound connection is allowed if
          either the range or the tag of the source matches.
      sourceTags:
          A list of instance tags which this rule applies to. One or
          both of sourceRanges and sourceTags may be set; an inbound
          connection is allowed if either the range or the tag of the
          source matches.
      targetTags:
          A list of instance tags indicating sets of instances
          located on network which may make network connections as
          specified in allowed. If no targetTags are specified, the
          firewall rule applies to all instances on the specified
          network.
      description:
          An optional textual description of the resource; provided
          by the client when the resource is created.
      names:
          List of names of objects to patch.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: List of Operation objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_patch_firewall_request(firewall, network, allowed, sourceRanges, sourceTags, targetTags, description, name, project, blocking)
        for firewall, name in gce_base.GoogleComputeEngineBase._combine(firewalls, names)], blocking))

  def __build_delete_firewall_request(self, firewall=None, project=None, blocking=True):
    # Unpacks firewall if its type is Firewall or dict.
    if isinstance(firewall, Firewall):
      firewall = firewall.name
    elif isinstance(firewall, dict):
      firewall = firewall.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not firewall:
      raise ValueError('firewall is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('DELETE', str(project) + '/firewalls/' + str(firewall), None, None)

  def delete_firewall(self, firewall=None, project=None, blocking=True):
    """Deletes the specified firewall resource.

    Args:
      firewall:
          Name of the firewall resource to delete.
          Or: Firewall to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Firewall or a JSON
          describing the resource.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    return self._parse(self._execute(self.__build_delete_firewall_request(
        firewall, project, blocking), blocking))

  def delete_firewalls(self, firewalls=None, project=None, blocking=True):
    """Deletes the specified firewall resource. List operation.

    Args:
      firewalls:
          List of firewalls to delete.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: List of Operation objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_delete_firewall_request(firewall, project, blocking)
        for firewall in firewalls], blocking))

  def __build_insert_network_request(self, network=None, IPv4Range=None, gatewayIPv4=None, description=None, name=None, project=None, blocking=True):
    # Unpacks network if its type is Network or dict.
    if isinstance(network, Network):
      if IPv4Range is None:
        IPv4Range = network.IPv4Range
      if gatewayIPv4 is None:
        gatewayIPv4 = network.gatewayIPv4
      if description is None:
        description = network.description
      if name is None:
        name = network.name
    elif isinstance(network, dict):
      if IPv4Range is None:
        IPv4Range = network.get('IPv4Range')
      if gatewayIPv4 is None:
        gatewayIPv4 = network.get('gatewayIPv4')
      if description is None:
        description = network.get('description')
      if name is None:
        name = network.get('name')
    elif isinstance(network, basestring):
      if name is not None and network != name:
        raise ValueError('Conflicting values of network and name supplied.')
      name = network

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not IPv4Range:
      raise ValueError('IPv4Range is a required parameter.')
    if not name:
      raise ValueError('name is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')

    # Creates a dict that will be sent in the request body.
    request = {
        'kind': 'compute#network',
        'IPv4Range': IPv4Range,
        'name': name
    }
    if gatewayIPv4:
      request['gatewayIPv4'] = gatewayIPv4
    if description:
      request['description'] = description
    return gce_base.GoogleComputeEngineBase.API_REQUEST('POST', str(project) + '/networks', None, json.dumps(request))

  def insert_network(self, network=None, IPv4Range=None, gatewayIPv4=None, description=None, name=None, project=None, blocking=True):
    """Creates a network resource in the specified project using the
    data included in the request.

    Args:
      network:
          Network to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Network or a JSON
          describing the resource.
      IPv4Range:
          Required; The range of internal addresses that are legal on
          this network. This range is a CIDR specification, for
          example: 192.168.0.0/16. Provided by the client when the
          network is created.
      gatewayIPv4:
          An optional address that is used for default routing to
          other networks. This must be within the range specified by
          IPv4Range, and is typically the first usable address in
          that range. If not specified, the default value is the
          first usable address in IPv4Range.
      description:
          An optional textual description of the resource; provided
          by the client when the resource is created.
      name:
          Name of the resource; provided by the client when the
          resource is created. The name must be 1-63 characters long,
          and comply with RFC1035.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    return self._parse(self._execute(self.__build_insert_network_request(
        network, IPv4Range, gatewayIPv4, description, name, project, blocking), blocking))

  def insert_networks(self, networks=None, IPv4Range=None, gatewayIPv4=None, description=None, names=None, project=None, blocking=True):
    """Creates a network resource in the specified project using the
    data included in the request. List operation.

    Args:
      networks:
          List of networks to insert.
      IPv4Range:
          Required; The range of internal addresses that are legal on
          this network. This range is a CIDR specification, for
          example: 192.168.0.0/16. Provided by the client when the
          network is created.
      gatewayIPv4:
          An optional address that is used for default routing to
          other networks. This must be within the range specified by
          IPv4Range, and is typically the first usable address in
          that range. If not specified, the default value is the
          first usable address in IPv4Range.
      description:
          An optional textual description of the resource; provided
          by the client when the resource is created.
      names:
          List of names of objects to insert.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: List of Operation objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_insert_network_request(network, IPv4Range, gatewayIPv4, description, name, project, blocking)
        for network, name in gce_base.GoogleComputeEngineBase._combine(networks, names)], blocking))

  def __build_get_network_request(self, network=None, project=None):
    # Unpacks network if its type is Network or dict.
    if isinstance(network, Network):
      network = network.name
    elif isinstance(network, dict):
      network = network.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not network:
      raise ValueError('network is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/networks/' + str(network), None, None)

  def get_network(self, network=None, project=None):
    """Returns the specified network resource.

    Args:
      network:
          Name of the network resource to return.
          Or: Network to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Network or a JSON
          describing the resource.
      project:
          Name of the project scoping this request.

    Returns: Network
    """
    return self._parse(self._execute(self.__build_get_network_request(
        network, project), False))

  def get_networks(self, networks=None, project=None):
    """Returns the specified network resource. List operation.

    Args:
      networks:
          List of networks to get.
      project:
          Name of the project scoping this request.

    Returns: List of Network objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_get_network_request(network, project)
        for network in networks], False))

  def list_networks(self, filter=None, project=None, maxResults=None, pageToken=None):
    """Retrieves the list of network resources available to the
    specified project.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.
      maxResults:
          Optional. Maximum count of results to be returned. Maximum
          and default value is 100.
      pageToken:
          Optional. Tag returned by a previous list request truncated
          by maxResults. Used to continue a previous list request.

    Returns: NetworkList
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    if maxResults:
      query_params['maxResults'] = maxResults
    if pageToken:
      query_params['pageToken'] = pageToken
    return self._parse(self._execute(gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project) + '/networks', query_params, None), False))

  def all_networks(self, filter=None, project=None):
    """Returns an iterator yielding all networks in a project that match
    specified criteria.

    Args:
      filter:
          Optional. Filter expression for filtering listed resources.
      project:
          Name of the project scoping this request.

    Returns: A generator of all networks.
    """
    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Processes the query parameters, if any.
    query_params = {}
    if filter:
      query_params['filter'] = filter
    return self._generate('GET', str(project) + '/networks', query_params, Network)

  def __build_delete_network_request(self, network=None, project=None, blocking=True):
    # Unpacks network if its type is Network or dict.
    if isinstance(network, Network):
      network = network.name
    elif isinstance(network, dict):
      network = network.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not network:
      raise ValueError('network is a required parameter.')
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('DELETE', str(project) + '/networks/' + str(network), None, None)

  def delete_network(self, network=None, project=None, blocking=True):
    """Deletes the specified network resource.

    Args:
      network:
          Name of the network resource to delete.
          Or: Network to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Network or a JSON
          describing the resource.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: Operation
    """
    return self._parse(self._execute(self.__build_delete_network_request(
        network, project, blocking), blocking))

  def delete_networks(self, networks=None, project=None, blocking=True):
    """Deletes the specified network resource. List operation.

    Args:
      networks:
          List of networks to delete.
      project:
          Name of the project scoping this request.
      blocking:
          If True, this method will block until the operation
          completes. This is True by default.

    Returns: List of Operation objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_delete_network_request(network, project, blocking)
        for network in networks], blocking))

  def set_common_instance_metadata(self, project=None, items=None):
    """Sets metadata common to all instances within the specified
    project using the data included in the request.

    Args:
      project:
          Name of the project scoping this request.
          Or: Project to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Project or a JSON
          describing the resource.
      items:
          Array of key/value pairs. The total size of all keys and
          values must be less than 512 KB.
    """
    # Unpacks project if its type is Project or dict.
    if isinstance(project, Project):
      project = project.name
    elif isinstance(project, dict):
      project = project.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')

    # Creates a dict that will be sent in the request body.
    request = {
        'kind': 'compute#metadata'
    }
    if items:
      request['items'] = _Item.array_to_json(items)
    return self._parse(self._execute(gce_base.GoogleComputeEngineBase.API_REQUEST('POST', str(project) + '/set-common-instance-metadata', None, json.dumps(request)), False))

  def __build_get_project_request(self, project=None):
    # Unpacks project if its type is Project or dict.
    if isinstance(project, Project):
      project = project.name
    elif isinstance(project, dict):
      project = project.get('name')

    # Applies global defaults to missing values.
    if project is None:
      project = self.default_project

    # Ensures all required parameters are present.
    if not project:
      raise ValueError('project is a required parameter.')
    return gce_base.GoogleComputeEngineBase.API_REQUEST('GET', str(project), None, None)

  def get_project(self, project=None):
    """Returns the specified project resource.

    Args:
      project:
          Name of the project resource to retrieve.
          Or: Project to use as a template. Other directly provided
          parameters take precedence and override any values in the
          template. May be an instance of Project or a JSON
          describing the resource.

    Returns: Project
    """
    return self._parse(self._execute(self.__build_get_project_request(
        project), False))

  def get_projects(self, projects=None):
    """Returns the specified project resource. List operation.

    Args:
      projects:
          List of projects to get.

    Returns: List of Project objects.
    """
    return self._parse_list(self._execute_list([
        self.__build_get_project_request(project)
        for project in projects], False))

