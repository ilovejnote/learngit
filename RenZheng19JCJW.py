任职能力认证教材（基础建维专业）
	第一篇职责规范
		1.1 县公司运维部职责
			001-县公司运维部职责
				1、 负责全网设备的维护以及工程建设进度、质量、安全、环评管理、验收工作；
				2、 负责全网运行的各类设备进行故障处理，网络安全生产，应急通信保障；
				3、 负责本地代维的管理工作及合作单位考核管理；
				4、 负责网络运行分析和网络质量管理，收集上报网络投诉并协调解决；
				5、 负责基站、机房、室分建设选址、协调、随工、施工进度管理及相关配套设施建设的验收，按时完成相关的建设工作；
				6、 负责装维工作全流程管理及实施工作，包括立项、建设进度，安全、环评、验收、转资等；
				7、 负责传输线路设计、建设、协调、随工、施工进度管理等，按时完成相关建设工作。
				8、 负责各类工程建设施工现场监督、随工、安全管理、验收，资料存档等。负责当地应急物资及施工现场物料的管理工作；
				9、 负责家客集客资源点申请立项工作，家客集客售前、售中、售后等技术支持等工作
				10、 负责网络基础维护，网络优化、网络投诉处理，网络测试等；
				11、 负责综合资管录入与审核，考核管理。
				12、 负责基站、传输线路的巡检，隐患上报、维修，更换电缆等，做好资产管理、安全生产等工作；
				13、 负责基站维修费、电费、租赁费等结算；
				14、 负责备品备件、应急物资等管理；
	第二篇专业知识
		2.1 电信网基础知识
			2.1.1  移动通信网
				一、通信网的分类
					001-我们可以根据通信网提供的业务类型，采用的交换技术、传输技术、服务范围、运营方式、拓扑结构等方面的不同来对其进行各种分类。 001
					002-
					按业务类型，可以将通信网分为电话通信网（如 PSTN、移动通信网等）、数据通信网（如X.25、Internet、帧中继网等）、广播电视网等 002
					003-
					按空间距离，可以将通信网分为广域网（WAN: Wide Area Network）、城域网（MAN:Metropolitan Area Network）和局域网（LAN: Local Area Network） 003
					004-
					按信号传输方式，可以将通信网分为模拟通信网和数字通信网 004 
					005-
					按运营方式，可以将通信网分为公用通信网和专用通信网 005
					006-					从管理和工程的角度看，网络之间本质的区别在于所采用的实现技术的不同，其主要包括三方面：交换技术、控制技术以及业务实现方式 006
			2.1.2 GSM   通信原理
				一、GSM  系统的主要特点：
					001-
					GSM 全名为：Global System for Mobile Communications，中文为全球移动通讯系统，俗称"全球通"，是第二代移动通信技术。 001 
					002-
					GSM 系统由几个分系统组成，各分系统之间都有定义明确且详细的标准化接口方案，保证任何厂商提供的 GSM 系统设备可以互连。 002
					003-
					采用 FDMA/TDMA及跳频的复用方式，频谱重复利用率较高，同时具有灵活方便的组网结构，可满足用户的不同容量需求003 
					004-
					具有较强的鉴权和加密功能，能确保用户和网络的安全需求，安全性较高。004
					005-
					抗干扰能力较强，系统的通信质量较高。 005
					006-
					除了可以开放基本的话音业务外，还可以开放各种承载业务、补充业务以及与 ISDN相关的各种业务。 006
				二、系统架构
					007-
					GSM 网络结构包括交换网络子系统（NSS）、无线基站子系统（BSS）、操作维护子系统（OSS）和移动台（MS）四大部分。 007
					008-
					 BSS 部分包括有基站控制器（BSC）、基站收发信台（BTS）和码型转换单元（TC）； 008
					009-
					NSS 部分包括有移动业务交换中心（MSC）、拜访位置寄存器（VLR）、归属位置寄存器（HLR）、鉴权中心（AUC）和移动设备识别寄存器（EIR）； 009
					010-
					OSS 部分包括有操作与维护中心-无线部分（OMC-R）、操作与维护中心-移动部分（OMC-M）和操作与维护中心-交换部分（OMC-S）； 010 
					011-
					移动台部分（MS），其中包括移动终端（MT）和客户识别卡（SIM）。011
					（1）无线基站子系统
					012-
					BSS 系统是在一定的无线覆盖区中，由 MSC 控制，与 MS 进行通信的系统设备，它主要负责完成无线发送接收和无线资源管理等功能。它给 MS 和 NSS 之间提供了传输通道并管理这个通道。 012
					013-
					BTS 包括收发信机和天线,以及与无线接口有关的信号处理电路等无线接口设备，013 
					014-
					BTS 它完全由 BSC 控制， 014
					015-
					BTS 主要负责无线传输，完成无线与有线的转换、无线分集、无线信道加密、跳频等功能。 015
					016-
					BSC：主要负责控制和管理,主要由 BTS 控制部分、交换部分和公共处理器部分等组成。016 
					017-
					BSC：具有对一个或多个 BTS 进行控制和管理的功能，它主要是进行无线信道的分配,释放以及越区信道切换的管理等,起中 BSS 系统中交换设备的作用。 017
					018-
					TC：具有码型转换，速率适配的功能。 018
					（2） 交换网络子系统
					019-
					交换网路子系统（NSS）包括实现 GSM 的主要交换功能的交换中心以及管理用户数据和移动性的所需的数据库。 019 
					（3）操作维护子系统
					020-
					GSM 系统的操作维护子系统（OMC），它主要是对整个 GSM 网络进行管理和监控。 020
					（4） 移动台
					021-
					移动终端就是“机”，它可完成话音编码、信道编码、信息加密、信息的调制和解调、信息发射和接收，以及实现鉴权、位置更新等通信处理。 021
					022-
					SIM 卡存有认证客户身份所需的所有信息，并能执行一些与安全保密有关的重要信息，以防止非法客户进入网络。 022					
					023-
					只有插入 SIM 后移动终端才能接入进网， 023 
					024-
					GSM 系统的主要接口系指 A 接口、Abis 接口和 Um 接口。 024 
					025-
					A 接口定义为网路子系统(NSS)与基站子系统(BSS)间的通信接口。 025
					026-
					Abis 接口定义了基站子系统(BSS)中基站控制器(BSC)和基站收发信台(BTS)之间的通信标准，用于远端互连方式。 026
					027-
					Um 接口(空中接口)定义为移动台与基站收发信台(BTS)之间的通信接口， 027
				三、GSM  的编号和识别方案
					1 、 GSM  位置区域的概念
					028-
					服务区系指移动台可获得服务的区域。028
					029-
					PLMN 区是指整个陆地移动通信网的地理区域。029
					030-
					MSC区指由一个移动业务交换中心所控制的所有小区共覆盖的区域构成的 PLMN 网的一部分。030
					031-
					一个 MSC 区可由若干位置区构成。 031
					032-
					位置区:指移动台可任意移动不需要进行位置更新的区域， 032 
					033-
					一个位置区可由若干个小区（或基站区）组成。 033
					034-
					基站区：由置于同一区域的一个或数个基站收发信台(BTS)包括的所有小区所覆盖的区域。 034
					035-
					小区：采用基站识别码或全球小区识别码进行标识的无线覆盖区域。035
					036-
					2、位置区和基站的识别
					037-
					在 GSM 系统中，共有三个号码组成对移动台的位置识别：LAI，CGI，BSIC。 037
					038-
					在检测位置更新和切换的需求时，要使用位置区识别 LAI ， 038 
					039-
					MCC－移动国家码， 039
					040-
					MNC－移动网号， 040
					041-
					LAC－位置区码， 041
					042-
					CGI是在所有GSM PLMN中作为小区的唯一标识，是在LAI的基础上再加上小区识别(CI)，042
					043-
					基站识别色码(BSIC)：用于识别相邻国家的相邻基站， 043 
				四、GSM 无线接口理论
					1工作频段的分配
					044-
					我国陆地蜂窝数字移动通信网 GSM 通信系统采用 900MHz 和 1800MHz 频段。 044
					045-
					900MHz 频段为：890~915MHz（移动台发，基站收）935~960MHz （基站发，移动台发） 045
					046-
					1800MHz 频段为：1710~1785MHz（移动台发，基站收）1805~1880MHz （基站发，移动台发） 046
#					047-
#					表 2-1 GSM 网络的工作频段 047
					048-
					相邻两频点间隔为 200KHz，每个频点采用时分多址（TDMA）方式，分为 8 个时隙，即 8个信道（全速率：13kbit/s）， 048
					049-
					若 GSM 采用半速率话音编码后，每个频点可容纳 16 个半速率信道，可使系统容量扩大一倍，但会导致语音质量降低。 049
					2 、 GSM 的 TDMA  信道的概念
					050-
					在 GSM 中的信道分为物理信道和逻辑信道， 050 
					051-
					一个物理信道就为一个时隙(TS)， 051 
					052-
					这些逻辑信道映射到物理信道上传送。从 BTS 到 MS 的方向称为下行链路，相反的方向称为上行链路。052 
					053-
					逻辑信道又分为两大类，业务信道和控制信道。 053
					（1）业务信道
					054-
					业务信道用于传送编码后的话音或客户数据，在上行和下行信道上，点对点（BTS 对一个 MS，或反之）方式传播。 054 
					055-
					业务信道用于携载语音或用户数据，可分为话音业务信道和数据业务信道。 055
					（2）控制信道（CCH）
					056-
					控制信道：用于传送信令或同步数据。根据所需完成的功能又把控制信道定义成广播控制信道（BCH）、公共控制信道（CCCH）和专用控制信道（DCCH） 056
			2.1.3 TD-LTE  通信原理
				二、TD-LTE  系统的主要特点
					001-
					1、通信速率有了提高，下行峰值速率为 100Mbps，上行为 50Mbps。 001
					002-
					2、提高了频谱效率，下行链路 5(bit/s)/Hz，上行链路 2.5(bit/s)/Hz。 002
					003-
					3、简单的网络架构和软件架构，以信道共用为基础，以分组域业务为主要目标，系统在整体架构上将基于 IP 分组交换。 003
					004-
					4、QoS 保证，通过系统设计和严格的 QoS 机制，保证实时业务(如 VoIP) 的服务质量。004
					005-
					5、系统部署灵活，能够支持 1.4～20MHz 间的多种系统带宽，保证了将来在系统部署上的灵活性。 005
					006-
					6、非常低的线网络时延。子帧长度为 0.5ms 和 0.675ms，解决了向下兼容的问题并降低了网络时延，时延可达 U-plan<5ms，C-plan<100ms。 006
					007-
					7、增加了小区边界比特速率，在保持目前基站位置不变的情况下增加小区边界比特速率，OFDM 支持的单频率网络技术可提供高效率的多播服务。 007
					008-
					8、强调向下兼容，支持已有的 3G 系统和非 3GPP 规范系统的协同运作，支持自组网（Self-organising Network）操作。 008
				三、系统架构
					009-
					eNodeB 之间通过 X2 接口互连 009
				四、工作频段
					010-
					F 频段（band 39） 1880-1900MHz 010
					011-
					E 频段（band 40） 2300-2400MHz 011
					012-
					D 频段（band 41） 2570-2620MHz 012
				五、TD-LTE  关键技术
					013-
					1. 频域多址技术 — OFDM/SC-FDMA
					2. MIMO 技术
					3. 高阶调制技术
					4. HARQ 技术
					5. 链路自适应技术 — AMC
					6. 快速 MAC 调度技术 013
			2.1.4 5G 基础知识
					001-
					5G 是面向 2020 年以后移动通信需求而发展的新一代移动通信系统，即第五代移动通信技术，是 4G 之后的延伸。5G 区别于 2G/3G/4G 的地方在于，它不仅是移动通信技术的顺序提升，更是多种无线接入技术演进集成后解决方案的总称 001 
					002-
					根据移动通信的发展规律，5G将具有超高的频谱利用率和能效,在传输速率和资源利用率等方面较 4G 移动通信提高一个
					量级或更高,其无线覆盖性能、传输时延、系统安全和用户体验也将得到显著的提高 002 
					003-
					体积减小重量增加。5G Massive MIMO 基站 AAU 频段更高、收发单元更多，与 4G 基站RRU+天线相比，挡风面积略有减小、重量略有增加（详见表 2），不会对现有塔型设计、铁塔承载造成额外的影响。主要的影响体现在 5G Massive MIMO 基站 AAU 采用 RRU 和天线一体化设计，不能与现有站点上的 2/3/4G 频段共天线，对部分共享需求旺盛的站点，会加剧天面资源紧张的局面。 003
					004-
					由于 5G 基站的射频指标要求尚未制定，5G 基站与其他系统的隔离度暂无标准，根据运营商的需求设置。 004
					005-
					进一步挖掘新的频率资源 (如高频段、毫米波与可见光等),使未来无线移动通信的频率资源扩展 4 倍左右 005
			2.2  全业务相关知识
				2.2.1 IP  基础知识
					一、  计算机网络的组成
					1. 网络传输介质
					001-
					有四种主要的网络传输介质：双绞线电缆、光纤、微波、同轴电缆。 001
					3.网络互联设备
					002-
					网络互联设备主要是指路由器 002 
					二、计算机网络的分类
					1 ．根据计算机网络覆盖的地理范围分类
					003-
					计算机网络可分为：局域网、城域网和广域网。 003 
					2 ．根据网络拓朴结构分类
					004-
					网络按照拓朴结构划分有：总线型结构、环型结构、星型结构、树型结构和网状结构。004
				2.2.2 GPON  基础知识
					一、  GPON  网元类型及架构
					1.GPON  概述
					001-
					ODN 网络覆盖距离大于 20Km， 001 
					002-
					提供 1.25G和 2.5G 的下行速率和所有标准上行速率，距离 20km，分路比 1:16～1:64，可扩展到 1:128。002
					2. GPON  典型应用方案
					003-
					GPON 系统通常由局侧的 OLT、用户侧的 ONU 和 ODN 组成，通常采用点到多点的网络结构。ODN 由单模光纤和光分路器、光连接器等无源光器件组成，为 OLT 和 ONU 之间的物理连接提供光传输媒质。 003
					004-
					按照 ONU 在接入网中所处的位置不同，GPON 系统可以有如下几种典型应用方案：
					（1）光纤到家庭用户(FTTH)：仅利用光纤传输媒质连接通信局端和家庭住宅的接入方式，引入光纤由单个家庭住宅独享。
					（2）光纤到公司/办公室(FTTO)：仅利用光纤传输媒质连接通信局端和公司或办公室用户的接入方式，引入光纤由单个公司或办公室用户独享，ONU/ONT 之后的设备或网络由用户管理。
					（3）光纤到楼宇/分线盒(FTTB/C)：以光纤替换用户引入点之前的铜线电缆，ONU 部署在传统的分线盒（用户引入点）即 DP 点（DP distribution point 分配点），ONU 下采用其他介质接入用户。
					（4）光纤到交接箱(FTTCab):以光纤替换传统馈线电缆，ONU 部署在交接箱即 FP 点处，ONU下采用其他介质接入到用户。 004
					二、  GPON  工作原理: :
					005-
					1  下行数据：
					广播方式：GPON 的下行帧长为固定的 125us，下行为广播方式，所有的 ONU 都能收到相同的数据，但是通过 ONUID 来区分不同的 ONU 的数据，ONU 通过过滤来接收属于自己的数据。005
					006-
					2  上行数据：
					TDMA 方式：GPON 的上行是通过 TDMA（时分复用）的方式传输数据，上行链路被分成不同的时隙，根据下行帧的 upstream bandwidth map 字段来给每个 ONU 分配上行时隙，这样所有的 ONU 就可以按照一定的秩序发送自己的数据了，不会产生为了争夺时隙而冲突。每帧共有 9120 个时隙。 006
				2.2.3  集客支撑网络及专线产品接入
					一、互联网专线
					IP 城域网承载互联网专线业务架构
					001-
					1、GPON  接入方式 001该方案要求客户侧上游汇聚点机房中必须有 OLT 设备。
					2、PTN  接入方式 001当 GPON 资源不满足时,优先考虑采用此类方案。
					3、SDH  接入方式 001当 GPON 和 PTN 模式不满足的情况下选择 SDH 方案。
					4、光纤直驱的接入方式 001该方案实现方式简单，易于开通，但可靠性较差，
					二、数据专线业务
					002-
					目前数据专线业务有单点对单点，一点对多点两种模式。 002
					003-
					PTN  多业务承载
					以分组为主的多业务传送，可同时对 2G、3G、集团客户、WLAN 业务实现综合承载；可提供多种接口：FE、GE、10GE；E1、STM-N。 003
					三、融合通信
					004-
					目前我公司语音采用 IMS 接入模式，带宽需求一般为 2M，传输方式与互联网业务相同。 004
					四、 IDC  业务
					005-
					1  概念及特点
					高品质的机房设施
					充沛稳定的电力供应
					高可靠性的网络联接
					与各大 ISP 网络的高速互联互通
					SLA 的服务品质保证
					专业化的网管监控、7*24 专业人员运维服务；机房 7＊24 小时有人值守
					防火墙、入侵检测、安全修补等增强性安全服务选用
					优化资源、降低成本、不必投巨资建设自已的机房
					共享专业化的网管系统、7*24 专业运维及安全服务、大容量的网络带宽及存储
					建立良好的企业形象及使企业 IT 系统的维护和升级流程简约化 005
				2.2.4 集客专线常见设备
					001-
					一、 接入层常见末端设备
					1  光纤收发器（光猫） 001
					2  协议转换器 001
					3  MSAP 001
#					002-
#					SDH/MSTP、PTN 技术特点比较表 002
				2.2.5 不同等级客户产品及维护标准、性能指标
					001-
					客户服务等级分为四个等级，分别为金牌级服务、银牌级服务、铜牌级服务和标准级服务。 001
					业务保障等级主要依据客户服务等级和客户业务的重要程度，分为 AAA 级、AA 级、A级和普通级四个级别。 001
#					002-
#					服务等级与业务保障等级的对应关系
					003-
					